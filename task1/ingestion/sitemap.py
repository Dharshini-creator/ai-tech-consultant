

import requests
import xml.etree.ElementTree as ET

SITEMAP_URL = "https://support.brilliantdirectories.com/support/sitemap.xml"


def get_article_urls():
    response = requests.get(
        SITEMAP_URL,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()

    root = ET.fromstring(response.content)
    urls = []

    for element in root.iter():
        if element.tag.endswith("loc") and element.text:
            url = element.text.strip()

            if "/support/solutions/articles/" in url:
                urls.append(url)

    return list(dict.fromkeys(urls))


if __name__ == "__main__":
    try:
        article_urls = get_article_urls()

        print(f"Individual article URLs found: {len(article_urls)}")
        print("\nFirst 10 article URLs:\n")

        for url in article_urls[:10]:
            print(url)

    except requests.RequestException as error:
        print(f"Website request failed: {error}")
    except ET.ParseError as error:
        print(f"Could not read sitemap XML: {error}")
