
import requests
from bs4 import BeautifulSoup


def download_article(url):
    try:
        response = requests.get(
            url,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the actual article body.
        article_body = soup.select_one("article#article-body")

        if article_body is None:
            print(f"Article content not found: {url}")
            return None

        # Remove unwanted elements inside the article.
        for element in article_body.select(
            "script, style, nav, footer, header"
        ):
            element.decompose()

        title_tag = soup.select_one(
            "#article-show-12000065940 h1, "
            "#article-body h1, "
            "h1"
        )

        title = (
            title_tag.get_text(" ", strip=True)
            if title_tag
            else soup.title.get_text(" ", strip=True)
            if soup.title
            else url
        )

        content = article_body.get_text(
            separator="\n",
            strip=True,
        )

        return {
            "url": url,
            "title": title,
            "content": content,
        }

    except requests.RequestException as error:
        print(f"Could not download {url}: {error}")
        return None


if __name__ == "__main__":
    test_url = (
        "https://support.brilliantdirectories.com/support/solutions/"
        "articles/12000065940-guide-1-how-to-connect-a-live-domain-name"
    )

    article = download_article(test_url)

    if article:
        print("TITLE:", article["title"])
        print("\nCONTENT LENGTH:", len(article["content"]))
        print("\nCONTENT PREVIEW:\n")
        print(article["content"][:1500])
