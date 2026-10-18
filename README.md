# AI Tech Consultant

A Python project with three connected tools for support knowledge search, email analysis, and meeting-to-scope extraction.

## Task 1: Knowledge Brain
- Stores 1,537 support article records from Brilliant Directories.
- Provides a FastAPI health check and keyword-based search API.
- API documentation: http://127.0.0.1:8000/docs

## Task 2: Inbox Agent
- Classifies sample emails by category and priority.
- Retrieves related articles from Task 1.
- Creates reply drafts for human approval, editing, or rejection.
- Does not send emails automatically.

## Task 3: Meeting to Scope
- Extracts requirements, deliverables, and open questions from meeting notes.
- Retrieves related articles from Task 1.
- Supports human approval, change requests, and rejection.

## Setup
Install dependencies from the project root:

```powershell
python -m pip install -r requirements.txt
```

## Run
Start the Knowledge Brain:

```powershell
.\run.ps1
```

Run the sample Inbox Agent:

```powershell
python task2\src\inbox_agent.py
```

Run the sample Meeting-to-Scope Agent:

```powershell
python task3\agents\scope_agent.py
```

## Tests
Run Task 2 tests:

```powershell
cd task2
python -m unittest discover -s tests -v
```

Run Task 3 tests:

```powershell
cd ..\task3
python -m unittest discover -s tests -v
```

## Current Limitations
The agents currently use keyword-based rules and templates. The project does not yet provide a live inbox, a complete interactive review interface, or a fully implemented Claude-powered workflow. Search uses keyword frequency rather than semantic similarity.
