\# Task 1: Knowledge Brain API Documentation



\## 1. Project Overview



The Knowledge Brain is a Python-based API that collects and searches support articles from the Brilliant Directories support website. It helps users find relevant information by entering keywords.



\## 2. Technologies Used



\- Python 3.13

\- FastAPI

\- Uvicorn

\- BeautifulSoup

\- JSON for storing article data



\## 3. Knowledge Base



\- Source: Brilliant Directories Support

\- Source URL: https://support.brilliantdirectories.com/support/sitemap.xml

\- Total articles collected: 1,537

\- Data file: `data/articles.json`



Each article contains:

\- Title

\- URL

\- Content



\## 4. API Endpoints



\### Health Check



\*\*Endpoint:\*\* `GET /health`



\*\*Purpose:\*\* Checks whether the API is running.



\*\*Example response:\*\*



```json

{

&#x20; "status": "healthy"

}

```



\*\*Test result:\*\* PASS — returned HTTP 200 OK.



\### Home



\*\*Endpoint:\*\* `GET /`



\*\*Purpose:\*\* Displays a welcome message and API status.



\### Search Articles



\*\*Endpoint:\*\* `GET /search`



\*\*Parameters:\*\*

\- `q`: Search keywords (required, minimum 2 characters).

\- `limit`: Maximum number of results (optional, default 5, maximum 20).



\*\*Example request:\*\*



`http://127.0.0.1:8000/search?q=email%20accounts\&limit=5`



\*\*Response fields:\*\*

\- `query`: Search query.

\- `total\_results`: Number of matching articles.

\- `results`: Matching article details.

\- `title`: Article title.

\- `url`: Article URL.

\- `snippet`: Article content preview.

\- `score`: Keyword match score.



\*\*Test result:\*\* PASS — returned HTTP 200 OK with matching search results.



\## 5. Running the API



Activate the virtual environment, navigate to the `task1` directory, and run:



```powershell

python -m uvicorn app.main:app --reload

```



Open the interactive API documentation at:



http://127.0.0.1:8000/docs



\## 6. Data Storage



Article data is stored in JSON format at:



`data/articles.json`



The API reads this file to search for relevant articles.



\## 7. Testing Summary



| Test | Expected Result | Status |

|---|---|---|

| Health check | `healthy` | PASS |

| Search endpoint | Matching article results | PASS |

| API startup | Application starts successfully | PASS |



\## 8. Conclusion



The Knowledge Brain API has been implemented and tested successfully. It provides health monitoring and keyword-based search across a knowledge base of 1,537 support articles.



This API forms the knowledge retrieval component of the AI Tech Consultant capstone project.

