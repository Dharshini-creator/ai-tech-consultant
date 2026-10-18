
import json
import time
from pathlib import Path

from ingestion.sitemap import get_article_urls
from ingestion.download_articles import download_article

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "articles.json"
PROGRESS_FILE = OUTPUT_DIR / "ingestion_progress.json"

BATCH_SIZE = 10
DELAY_SECONDS = 1


def load_saved_articles():
    if not OUTPUT_FILE.exists():
        return []

    try:
        with OUTPUT_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not read saved articles: {error}")
        raise


def save_articles(articles):
    temporary_file = OUTPUT_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False, indent=2)

    temporary_file.replace(OUTPUT_FILE)


def save_progress(processed, total, successful, failed):
    progress = {
        "processed": processed,
        "total": total,
        "successful": successful,
        "failed": failed,
    }

    with PROGRESS_FILE.open("w", encoding="utf-8") as file:
        json.dump(progress, file, indent=2)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    urls = get_article_urls()
    articles = load_saved_articles()

    saved_urls = {
        article.get("url")
        for article in articles
        if article.get("url")
    }

    remaining_urls = [
        url for url in urls
        if url not in saved_urls
    ]

    print(f"Total article URLs: {len(urls)}")
    print(f"Already saved: {len(saved_urls)}")
    print(f"Remaining: {len(remaining_urls)}")

    successful = len(saved_urls)
    failed = 0
    processed = 0

    try:
        for start in range(0, len(remaining_urls), BATCH_SIZE):
            batch = remaining_urls[start:start + BATCH_SIZE]

            for url in batch:
                processed += 1
                print(
                    f"[{processed}/{len(remaining_urls)}] "
                    f"Downloading: {url}",
                    flush=True,
                )

                article = download_article(url)

                if article and article.get("content", "").strip():
                    articles.append(article)
                    saved_urls.add(url)
                    successful += 1
                    print(f"  SAVED: {article['title']}", flush=True)
                else:
                    failed += 1
                    print("  FAILED: No article content", flush=True)

                time.sleep(DELAY_SECONDS)

            # Save successful articles after each batch.
            save_articles(articles)
            save_progress(processed, len(remaining_urls), successful, failed)

            print(
                f"\nProgress saved. Successful: {successful}; "
                f"failed this run: {failed}\n",
                flush=True,
            )

    except KeyboardInterrupt:
        print("\nStopped by user. Saving collected articles...")
        save_articles(articles)
        save_progress(processed, len(remaining_urls), successful, failed)

    save_articles(articles)
    save_progress(processed, len(remaining_urls), successful, failed)

    print("\nINGESTION SUMMARY")
    print(f"Successful articles: {successful}")
    print(f"Failed this run: {failed}")
    print(f"Article data: {OUTPUT_FILE}")
    print(f"Progress data: {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
