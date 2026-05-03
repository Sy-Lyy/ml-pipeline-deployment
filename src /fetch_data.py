"""Download BooksToScrape category pages with logging and simple CLI.

Examples (PowerShell):
    python src/fetch_data.py --all --outdir ".\\data\\raw"
    python src/fetch_data.py --categories mystery poetry --outdir ".\\data\\raw"
    python src/fetch_data.py --url "http://..." --output ".\\data\\raw\\download.html"

Notes:
- Creates timestamped logs under `./logs/fetch-YYYYMMDD.log`
- Original functionality remains identical; only documentation was added.
"""


import argparse
import logging
import sys
import time
import pathlib
import requests

CATEGORIES = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry":  "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html",
}

def setup_logging():
    """Configure console and file logging under `./logs`.

    Creates a daily log file `fetch-YYYYMMDD.log` and logs INFO-level events.
    """
    logdir = pathlib.Path("logs")
    logdir.mkdir(parents=True, exist_ok=True)
    logfile = logdir / f"fetch-{time.strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout),
                  logging.FileHandler(logfile, encoding="utf-8")]
    )
    logging.info("Logger initialized → %s", logfile.resolve())

def download(url: str, outpath: pathlib.Path):
    """Download a single webpage and save it to the given path.

    Args:
        url (str): Target URL.
        outpath (pathlib.Path): Destination file path.
    """
    outpath.parent.mkdir(parents=True, exist_ok=True)
    logging.info("Start download: %s", url)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    outpath.write_bytes(resp.content)
    logging.info("Saved → %s (%d bytes)", outpath.resolve(), len(resp.content))
    print(f"Saved HTML to {outpath}")

def parse_args():
    """Parse CLI arguments for fetching category pages.

    Returns:
        argparse.Namespace:
            --url (str): Full URL to fetch
            --output (str): Output filename
            --categories (list[str]): Category names (mystery, poetry, science)
            --all (flag): Fetch all predefined categories
            --outdir (str): Output directory (default: data/raw)
    """
    p = argparse.ArgumentParser(description="Fetch webpages with logging and CLI options.")
    p.add_argument("--url", help="Full URL to fetch")
    p.add_argument("--output", help="Output filepath")
    p.add_argument("--categories", nargs="+", choices=sorted(CATEGORIES.keys()))
    p.add_argument("--all", action="store_true")
    p.add_argument("--outdir", default="data/raw")
    return p.parse_args()

def main():
    """Main entry point.

    Initializes logging, parses CLI arguments, and downloads either a single URL
    or one or more predefined categories into the output directory.
    """
    setup_logging()
    args = parse_args()
    outdir = pathlib.Path(args.outdir)

    if args.url:
        ts = time.strftime("%Y%m%d-%H%M%S")
        outfile = pathlib.Path(args.output) if args.output else outdir / f"download-{ts}.html"
        download(args.url, outfile)
        return

    selected = sorted(CATEGORIES.keys()) if args.all else (args.categories or [])
    if not selected:
        logging.warning("No options given. Use --url or --categories or --all.")
        return

    ts = time.strftime("%Y%m%d-%H%M%S")
    for label in selected:
        url = CATEGORIES[label]
        outfile = outdir / f"{label}-{ts}.html"
        download(url, outfile)

if __name__ == "__main__":
    main()
