
from datetime import datetime


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

    return {
        "subject": subject,
        "sender": email.get("sender", "Unknown"),
        "priority": priority,
        "category": category,
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
