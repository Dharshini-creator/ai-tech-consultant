
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
app = FastAPI(
    title="Knowledge Brain API",
    description="An API for the AI Tech Consultant project",
    version="1.0.0",
)

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "articles.json"


def load_articles():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


@app.get("/")
def home():
    html_file = Path(__file__).resolve().parent / "static" / "index.html"
    return FileResponse(html_file)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.get("/search")
def search_articles(
    q: str = Query(..., min_length=2, description="Keywords to search for"),
    limit: int = Query(5, ge=1, le=20),
):
    articles = load_articles()

    if not articles:
        raise HTTPException(
            status_code=503,
            detail="Knowledge data is unavailable. Check data/articles.json.",
        )

    keywords = q.lower().split()
    results = []

    for article in articles:
        title = article.get("title", "")
        content = article.get("content", "")
        searchable_text = f"{title} {content}".lower()

        score = sum(searchable_text.count(word) for word in keywords)

        if score > 0:
            results.append({
                "title": title,
                "url": article.get("url", ""),
                "snippet": content[:350],
                "score": score,
            })

    results.sort(key=lambda item: item["score"], reverse=True)

    return {
        "query": q,
        "total_results": len(results),
        "results": results[:limit],
    }
