
import re


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
