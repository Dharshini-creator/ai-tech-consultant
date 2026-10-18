# AI Tech Consultant - System Design



## 1. Architecture Overview



The project consists of three independent components:



1\. Knowledge Brain - collects and searches support articles.

2\. Inbox Agent - analyzes emails and suggests replies.

3\. Meeting to Scope - converts meeting notes into structured project scope information.



## 2. Task 1: Knowledge Brain



### Data Ingestion



The ingestion pipeline retrieves article URLs from the Brilliant Directories support sitemap. It downloads article pages, extracts titles and content, and saves the results to a JSON file.



### Storage



Article data is stored in `task1/data/articles.json`. Each record contains a title, URL, and content.



### API



FastAPI exposes three endpoints:



- `GET /` - welcome message and application status.

- `GET /health` - health status.

- `GET /search?q=...\&limit=...` - keyword-based article search.



The search endpoint counts keyword occurrences in article titles and content, sorts the results by score, and returns a limited list of matches.



## 3. Task 2: Inbox Agent



The Inbox Agent receives an email represented as a Python dictionary.



Processing steps:



1\. Read the email subject and body.

2\. Detect urgent keywords.

3\. Assign high or normal priority.

4\. Categorize the email as billing, meeting, support, or general.

5\. Generate a suggested reply.

6\. Return the analysis as a dictionary.



The current implementation uses predefined keyword rules and sample email data.



## 4. Task 3: Meeting to Scope



The Meeting to Scope agent receives meeting notes as text.



Processing steps:



1\. Split the notes into individual lines.

2\. Identify open questions and uncertain items.

3\. Identify planned deliverables.

4\. Identify requirements.

5\. Return structured output containing requirements, deliverables, open questions, and original notes.



The current implementation uses keyword matching and simple text rules.



## 5. Error Handling and Reliability



- The Knowledge Brain API returns an error if its knowledge data is unavailable.

- The ingestion pipeline saves progress to support recovery after interruptions.

- Automated unit tests check important Inbox Agent and Meeting to Scope behaviors.

- API health checks help verify that the Knowledge Brain is running.



## 6. Security and Limitations



- The current components are prototypes and are not configured for production deployment.

- The email agent does not connect to or send messages through a real inbox.

- Keyword matching can misclassify ambiguous text.

- The search system does not yet use embeddings or semantic retrieval.

- Sensitive email information should not be logged or shared unnecessarily.



## 7. Future Improvements



- Add semantic search and relevance evaluation.

- Integrate an authorized email provider.

- Add human approval before sending any reply.

- Improve requirements extraction with an AI language model.

- Add broader automated tests and structured logging.

- Provide a web interface for users.
