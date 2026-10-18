

import requests
from bs4 import BeautifulSoup

url = "https://support.brilliantdirectories.com/support/solutions/12000001358"

response = requests.get(
    url,
    timeout=30,
    headers={"User-Agent": "Mozilla/5.0"},
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("PAGE TITLE:")
print(soup.title.get_text(strip=True) if soup.title else "No title")

print("\nHEADINGS:")
for heading in soup.find_all(["h1", "h2", "h3"]):
    text = heading.get_text(" ", strip=True)
    if text:
        print("-", text)

print("\nCONTENT CONTAINERS:")
for tag in soup.find_all(["article", "main"]):
    text = tag.get_text(" ", strip=True)
    if text:
        print(f"\n<{tag.name}>: {text[:500]}")
