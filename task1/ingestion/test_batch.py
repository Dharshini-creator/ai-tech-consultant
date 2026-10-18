
import json
import time
from pathlib import Path

from sitemap import get_article_urls
from download_articles import download_article

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "test_articles.json"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    urls = get_article_urls()[:5]
    articles = []

    print(f"Testing download of {len(urls)} articles...\n")

    for index, url in enumerate(urls, start=1):
        print(f"[{index}/{len(urls)}] Downloading: {url}")

        article = download_article(url)

        if article and article["content"].strip():
            articles.append(article)
            print(f"SUCCESS: {article['title']}")
            print(f"Characters: {len(article['content'])}")
        else:
            print("SKIPPED: No article content found.")

        print()
        time.sleep(1)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False, indent=2)

    print("=" * 50)
    print(f"Successful articles: {len(articles)} out of {len(urls)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
