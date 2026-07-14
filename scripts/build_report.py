"""Build self-contained HTML (+ optional PDF) from a report markdown file.

Usage:  python scripts/build_report.py reports/2026-annual-review.md [--no-pdf]
Output: reports/2026-annual-review.html (images embedded, print-styled)
        reports/2026-annual-review.pdf  (via headless Edge/Chrome/Chromium, if found)

Markdown stays the source of truth; run this at finalization (and after any
edit worth re-sharing). Requires: pip install markdown
The PDF step needs a Chromium-family browser (Edge, Chrome, Chromium, Brave);
if none is found the script writes the HTML and tells you — you can always
open the HTML in any browser and print to PDF yourself.
Set REPORT_BROWSER=/path/to/browser to use a specific one.
"""
import base64, mimetypes, os, pathlib, platform, re, shutil, subprocess, sys, tempfile

CSS = """
body { font-family: Segoe UI, -apple-system, Helvetica, Arial, sans-serif;
       color: #1f2328; max-width: 900px; margin: 2rem auto; padding: 0 1.5rem;
       line-height: 1.55; font-size: 15px; }
h1 { border-bottom: 2px solid #d1d9e0; padding-bottom: .3em; }
h2 { border-bottom: 1px solid #d1d9e0; padding-bottom: .25em; margin-top: 2em; }
h3 { margin-top: 1.6em; }
table { border-collapse: collapse; margin: 1em 0; width: 100%; font-size: 13.5px; }
th, td { border: 1px solid #d1d9e0; padding: 5px 9px; text-align: left; }
th { background: #f6f8fa; }
tr:nth-child(even) { background: #fbfcfd; }
img { max-width: 100%; height: auto; margin: .8em 0; }
code { background: #f6f8fa; padding: .1em .35em; border-radius: 4px; font-size: 90%; }
blockquote { color: #59636e; border-left: 3px solid #d1d9e0; margin-left: 0; padding-left: 1em; }
hr { border: none; border-top: 1px solid #d1d9e0; margin: 2em 0; }
a { color: #0969da; }
@media print {
  body { max-width: none; margin: 0; font-size: 11.5px; }
  table { font-size: 10px; page-break-inside: avoid; }
  img { page-break-inside: avoid; max-height: 88vh; }
  h2 { page-break-after: avoid; }
  a { color: inherit; text-decoration: none; }
}
"""


def find_browser() -> str | None:
    """Locate a Chromium-family browser across Windows/macOS/Linux."""
    env = os.environ.get("REPORT_BROWSER")
    if env and pathlib.Path(env).exists():
        return env

    for name in ("msedge", "microsoft-edge", "google-chrome", "google-chrome-stable",
                 "chromium", "chromium-browser", "brave-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path

    candidates: list[str] = []
    system = platform.system()
    if system == "Windows":
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"),
                     os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
                     os.environ.get("LocalAppData", "")):
            if base:
                candidates += [
                    rf"{base}\Microsoft\Edge\Application\msedge.exe",
                    rf"{base}\Google\Chrome\Application\chrome.exe",
                ]
    elif system == "Darwin":
        candidates += [
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        ]
    return next((c for c in candidates if pathlib.Path(c).exists()), None)


def build(md_path: pathlib.Path, make_pdf: bool = True) -> None:
    try:
        import markdown
    except ImportError:
        sys.exit("The 'markdown' package is required:  pip install markdown")

    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])

    # embed local images as base64 so the HTML is a single self-contained file
    def embed(m):
        src = m.group(1)
        img = (md_path.parent / src)
        if img.exists():
            mime = mimetypes.guess_type(img.name)[0] or "image/png"
            b64 = base64.b64encode(img.read_bytes()).decode()
            return m.group(0).replace(src, f"data:{mime};base64,{b64}")
        return m.group(0)
    html_body = re.sub(r'<img[^>]*?src="([^"]+)"', embed, html_body)

    title = re.search(r"<h1[^>]*>(.*?)</h1>", html_body)
    title = title.group(1) if title else md_path.stem
    html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<title>{title}</title><style>{CSS}</style></head>"
            f"<body>{html_body}</body></html>")
    out_html = md_path.with_suffix(".html")
    out_html.write_text(html, encoding="utf-8")
    print(f"wrote {out_html} ({len(html)//1024} KB)")

    if not make_pdf:
        return
    browser = find_browser()
    if not browser:
        print("no Edge/Chrome/Chromium found — skipped the PDF. Open the HTML in any "
              "browser and print to PDF, or set REPORT_BROWSER=/path/to/browser.")
        return
    out_pdf = md_path.with_suffix(".pdf")
    profile = pathlib.Path(tempfile.gettempdir()) / "report-pdf-profile"
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-first-run",
                    f"--user-data-dir={profile}",
                    "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf.resolve()}",
                    out_html.resolve().as_uri()], check=True, timeout=120)
    print(f"wrote {out_pdf} ({out_pdf.stat().st_size//1024} KB)")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--no-pdf"]
    if not args or "--help" in args or "-h" in args:
        sys.exit(__doc__)
    build(pathlib.Path(args[0]), make_pdf="--no-pdf" not in sys.argv)
