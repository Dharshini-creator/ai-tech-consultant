\# AI Tech Consultant



\## Project Overview



AI Tech Consultant is a Python-based project that demonstrates three tools for knowledge retrieval, email analysis, and meeting scope extraction.



\## Project Tasks



\### Task 1: Knowledge Brain



\- Collects 1,537 support articles from Brilliant Directories.

\- Stores article data in JSON format.

\- Provides a FastAPI application with health-check and keyword-search endpoints.

\- API documentation is available at `http://127.0.0.1:8000/docs` when the server is running.



\### Task 2: Inbox Agent



\- Identifies high-priority emails using keyword matching.

\- Categorizes emails as billing, meeting, support, or general.

\- Generates suggested replies for human review.

\- Includes automated unit tests.



\### Task 3: Meeting to Scope



\- Extracts project requirements from meeting notes.

\- Identifies planned deliverables.

\- Collects open questions and uncertain items.

\- Returns structured JSON output.

\- Includes automated unit tests.



\## Project Structure



```text

ai-tech-consultant/

├── task1/

│   ├── app/

│   ├── data/

│   ├── ingestion/

│   └── docs/

├── task2/

│   ├── src/

│   ├── tests/

│   └── docs/

├── task3/

│   ├── agents/

│   ├── app/

│   ├── tests/

│   └── docs/

├── shared-docs/

├── README.md

├── DESIGN.md

├── EVALS.md

└── AI\_LOG.md

```



\## Running the Components



\### Knowledge Brain



From the `task1` directory:



```powershell

python -m uvicorn app.main:app --reload

```



\### Inbox Agent



From the `task2` directory:



```powershell

python .\\src\\inbox\_agent.py

```



\### Meeting to Scope



From the `task3` directory:



```powershell

python .\\agents\\scope\_agent.py

```



\## Testing



Run the Inbox Agent tests from `task2`:



```powershell

python -m unittest discover -s tests -v

```



Run the Meeting to Scope tests from `task3`:



```powershell

python -m unittest discover -s tests -p "test\_scope\_agent.py" -v

```



\## Current Limitations



\- Email analysis uses sample data and does not connect to a live inbox.

\- Email categorization and meeting scope extraction use keyword-based rules.

\- Suggested replies are drafts and are not sent automatically.

\- Search results are based on keyword frequency rather than semantic similarity.



\## Conclusion



This project demonstrates foundational implementations of a knowledge search API, an inbox analysis agent, and a meeting scope extraction tool.

