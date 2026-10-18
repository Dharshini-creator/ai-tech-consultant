
import re
import os
import requests

def search_knowledge_brain(query):
    """Find relevant help articles using Task 1."""
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

def create_scope(meeting_notes):
    """Convert meeting notes into a structured project scope."""

    lines = [
        line.strip(" -*\t")
        for line in meeting_notes.splitlines()
        if line.strip()
    ]

    requirements = []
    deliverables = []
    questions = []
    knowledge_articles = search_knowledge_brain(meeting_notes)

    requirement_words = [
        "must", "need", "needs", "require", "required",
        "should", "shall", "will",
    ]
    deliverable_words = [
        "build", "create", "develop", "implement",
        "deliver", "design",
    ]
    question_words = [
        "unclear", "confirm", "decide", "unknown",
        "not sure", "tbd", "to be decided",
    ]

    for line in lines:
        lower_line = line.lower()

        if "?" in line or any(word in lower_line for word in question_words):
            questions.append(line)
        elif any(word in lower_line for word in deliverable_words):
            deliverables.append(line)
        elif any(word in lower_line for word in requirement_words):
            requirements.append(line)

    return {
        "project_name": "Meeting to Scope",
        "summary": (
            f"Processed {len(lines)} meeting notes and extracted "
            f"{len(requirements)} requirements, "
            f"{len(deliverables)} deliverables, and "
            f"{len(questions)} open questions."
        ),
        "requirements": requirements,
        "deliverables": deliverables,
        "open_questions": questions,
        "all_notes": lines,
        "knowledge_articles": knowledge_articles,
    }


if __name__ == "__main__":
    sample_notes = """
    Build a customer dashboard.
    The dashboard must support mobile devices.
    Create a weekly reporting feature.
    Confirm which users can access reports.
    The system should load quickly.
    """

    import json
    print(json.dumps(create_scope(sample_notes), indent=2))

def approve_scope(scope):
    """Approve a generated scope after human review."""
    scope["review_status"] = "approved"
    scope["approved"] = True
    return scope


def request_scope_changes(scope, feedback):
    """Record human feedback and return the scope for revision."""
    scope["review_status"] = "changes_requested"
    scope["approved"] = False
    scope["review_feedback"] = feedback
    return scope


def reject_scope(scope, reason):
    """Reject a generated scope."""
    scope["review_status"] = "rejected"
    scope["approved"] = False
    scope["review_feedback"] = reason
    return scope
