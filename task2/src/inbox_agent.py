
from datetime import datetime
import os
import requests

def search_knowledge_brain(query):
    """Search Task 1 for helpful articles related to an email."""
    api_url = os.getenv(
        "KNOWLEDGE_BRAIN_URL",
        "http://127.0.0.1:8000"
    )

    try:
        response = requests.get(
            f"{api_url}/search",
            params={"q": query, "limit": 5},
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            return data

        return data.get("results", data.get("articles", []))

    except (requests.RequestException, ValueError):
        return []
def analyze_email(email):
    """Analyze an email and suggest its priority and category."""

    subject = email.get("subject", "")
    body = email.get("body", "")
    text = f"{subject} {body}".lower()

    urgent_words = ["urgent", "asap", "immediately", "deadline"]
    categories = {
    "billing": ["invoice", "payment", "billing", "refund"],
    "meeting": ["meeting", "schedule", "calendar"],
    "support": ["issue", "problem", "error", "help"],
    "general": [],
}
    priority = (
        "high"
        if any(word in text for word in urgent_words)
        else "normal"
    )

    category = "general"
    for name, keywords in categories.items():
        if name != "general" and any(word in text for word in keywords):
            category = name
            break

    knowledge_articles = search_knowledge_brain(
         f"{subject} {body}"
    )

    return {
        "subject": subject,
        "sender": email.get("sender", "Unknown"),
         "review_status": "pending",
        "approved": False,
        "priority": priority,
        "category": category,
        "knowledge_articles": knowledge_articles,
        "analyzed_at": datetime.now().isoformat(timespec="seconds"),
        "suggested_reply": (
            f"Hello, thank you for your email about '{subject}'. "
            "I have received your message and will review it shortly."
        ),
    }


if __name__ == "__main__":
    sample_email = {
        "sender": "customer@example.com",
        "subject": "Urgent: Payment issue",
        "body": "Please help me resolve this payment problem ASAP.",
    }

    print(analyze_email(sample_email))
    
def approve_reply(result):
    """Approve a draft after a human reviews it."""
    result["review_status"] = "approved"
    result["approved"] = True
    return result


def edit_reply(result, new_reply):
    """Save a human-edited draft for review."""
    result["suggested_reply"] = new_reply
    result["review_status"] = "pending"
    result["approved"] = False
    return result


def reject_reply(result):
    """Reject a draft so it is not approved for sending."""
    result["review_status"] = "rejected"
    result["approved"] = False
    return result

