#!/usr/bin/env python3
"""
Fetch and extract brand-messaging markdown from GitHub blob pages.

Why a helper: the runtime blocks raw.githubusercontent.com and api.github.com
(network egress policy). The only path is github.com/.../blob/... HTML pages.
This script centralizes the extraction so SKILL.md stays readable.

Usage:
    python scripts/fetch_brand.py                    # fetch default six files
    python scripts/fetch_brand.py --file tone.md     # fetch one
    python scripts/fetch_brand.py --out brand/       # write to directory

Output:
    Markdown text to stdout (default) or to files under --out.

Exit codes:
    0 — all fetches and extractions succeeded
    1 — at least one file failed
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

DEFAULT_FILES = [
    "terminology.md",
    "tone.md",
    "narrative.md",
    "value-story.md",
    "positioning.md",
    "boilerplates.md",
]

BASE = "https://github.com/cruciate-hub/marketing-team/blob/main/messaging/"
USER_AGENT = "aeo-content/2 (+https://social.plus)"

# Tags whose close produces a newline in extracted markdown.
BLOCK_CLOSE_TAGS = {
    "p", "li", "ul", "ol", "tr", "thead", "tbody",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "pre", "blockquote", "div", "article",
}

# Tags whose entire content is code — preserve inner text as-is.
CODE_TAGS = {"pre", "code"}


# ------------------------------------------------------------
# Fetch
# ------------------------------------------------------------


def fetch(url: str, max_retries: int = 3) -> str:
    """Fetch a URL with exponential backoff on transient errors."""
    last: Exception | None = None
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            # 4xx is not retryable.
            if 400 <= e.code < 500:
                raise RuntimeError(f"HTTP {e.code} for {url}") from e
            last = e
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)  # 1s, 2s, 4s
    raise RuntimeError(f"fetch failed after {max_retries} attempts: {last}") from last


# ------------------------------------------------------------
# Extract — primary path uses html.parser; regex is the fallback.
# ------------------------------------------------------------


class MarkdownBodyExtractor(HTMLParser):
    """Extract text content from the <article class='markdown-body'> element.

    This is a pragmatic extractor: it produces readable plain text with
    paragraph breaks. It is not a perfect HTML-to-markdown converter, and
    doesn't need to be — the downstream consumer is an LLM reading brand
    messaging, not a Markdown renderer.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_target = False
        self.depth = 0
        self.parts: list[str] = []
        self.suppress = 0  # depth counter for script/style tags

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        if (
            not self.in_target
            and tag == "article"
            and "markdown-body" in attrs_dict.get("class", "")
        ):
            self.in_target = True
            self.depth = 1
            return
        if not self.in_target:
            return
        if tag in ("script", "style"):
            self.suppress += 1
            return
        if tag == "br":
            self.parts.append("\n")
            return
        self.depth += 1

    def handle_endtag(self, tag: str) -> None:
        if not self.in_target:
            return
        if tag in ("script", "style") and self.suppress > 0:
            self.suppress -= 1
            return
        if tag == "article" and self.depth <= 1:
            self.in_target = False
            return
        self.depth -= 1
        if tag in BLOCK_CLOSE_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.in_target and self.suppress == 0:
            self.parts.append(data)

    def get_text(self) -> str:
        text = "".join(self.parts)
        # Collapse 3+ consecutive newlines into 2.
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def extract_html_parser(html_text: str) -> str | None:
    try:
        extractor = MarkdownBodyExtractor()
        extractor.feed(html_text)
        text = extractor.get_text()
        return text or None
    except Exception:
        return None


def extract_regex(html_text: str) -> str:
    """Fallback extractor. Keeps working if GitHub changes inner markup slightly,
    as long as the outer <article class='markdown-body'> still exists.
    """
    m = re.search(
        r'<article[^>]*class="[^"]*markdown-body[^"]*"[^>]*>(.*?)</article>',
        html_text,
        re.DOTALL,
    )
    if not m:
        raise RuntimeError(
            "markdown-body element not found. GitHub may have changed its markup. "
            "Inspect the page source and update scripts/fetch_brand.py."
        )
    inner = m.group(1)
    inner = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", inner, flags=re.DOTALL | re.IGNORECASE)
    inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.IGNORECASE)
    inner = re.sub(
        r"</(h[1-6]|p|li|ul|ol|tr|pre|blockquote|div|article)>",
        "\n",
        inner,
        flags=re.IGNORECASE,
    )
    inner = re.sub(r"<[^>]+>", "", inner)
    text = html.unescape(inner).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def extract_markdown(html_text: str) -> str:
    """Try html.parser, fall back to regex. Raise if neither works."""
    primary = extract_html_parser(html_text)
    if primary:
        return primary
    return extract_regex(html_text)


def fetch_one(name: str) -> str:
    return extract_markdown(fetch(BASE + name))


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description="Fetch social.plus brand-messaging files")
    p.add_argument(
        "--file",
        action="append",
        help="Specific file(s) to fetch (default: all six)",
    )
    p.add_argument("--out", type=Path, help="Write each file to this directory")
    args = p.parse_args()

    files = args.file or DEFAULT_FILES
    failures: list[str] = []

    for name in files:
        try:
            text = fetch_one(name)
        except Exception as e:
            failures.append(f"{name}: {e}")
            continue
        if args.out:
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / name).write_text(text, encoding="utf-8")
            print(f"wrote {args.out / name}", file=sys.stderr)
        else:
            print(f"\n===== {name} =====\n")
            print(text)

    if failures:
        print("\nfailures:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
