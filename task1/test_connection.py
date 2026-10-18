
from ingestion.download_articles import download_article

test_urls = [
    "https://support.brilliantdirectories.com/support/solutions/articles/12000065940-guide-1-how-to-connect-a-live-domain-name",
    "https://support.brilliantdirectories.com/support/solutions/articles/12000019742-guide-2-how-to-configure-general-settings",
    "https://support.brilliantdirectories.com/support/solutions/articles/12000001966-how-to-submit-a-support-ticket",
]

for url in test_urls:
    print("\n" + "=" * 70)

    article = download_article(url)

    if article:
        print("TITLE:", article["title"])
        print("CONTENT LENGTH:", len(article["content"]))
        print("PREVIEW:", article["content"][:200].replace("\n", " "))
    else:
        print("FAILED:", url)
