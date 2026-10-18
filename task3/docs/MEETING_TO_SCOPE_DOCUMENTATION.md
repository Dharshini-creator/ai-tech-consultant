\# Task 3: Meeting to Scope Documentation



\## 1. Project Overview



Meeting to Scope is a Python tool that converts meeting notes into a structured project scope. It identifies requirements, deliverables, and open questions.



\## 2. Technologies Used



\- Python 3

\- Regular expressions module

\- JSON

\- Python unittest framework



\## 3. Features



\### Requirements Extraction



Identifies statements containing keywords such as must, need, required, should, shall, and will.



\### Deliverables Extraction



Identifies planned work using keywords such as build, create, develop, implement, deliver, and design.



\### Open Questions Extraction



Identifies questions and uncertain items using question marks and keywords such as confirm, unclear, decide, unknown, and TBD.



\### Structured Output



The agent returns:

\- Project name

\- Summary

\- Requirements

\- Deliverables

\- Open questions

\- Original meeting notes



\## 4. Project Structure



```text

task3/

├── agents/

│   └── scope\_agent.py

├── app/

├── tests/

│   └── test\_scope\_agent.py

└── docs/

&#x20;   └── MEETING\_TO\_SCOPE\_DOCUMENTATION.md

```



\## 5. How to Run



From the `task3` directory:



```powershell

python .\\agents\\scope\_agent.py

```



\## 6. How to Run Tests



```powershell

python -m unittest discover -s tests -p "test\_scope\_agent.py" -v

```



\## 7. Testing Results



| Test | Status |

|---|---|

| Requirements extraction | PASS |

| Deliverables extraction | PASS |

| Open questions extraction | PASS |



Total tests passed: 3.



\## 8. Current Limitations



\- The tool uses keyword-based rules rather than an AI language model.

\- A sentence may be classified incorrectly if it contains overlapping keywords.

\- Meeting notes should be clear and reasonably well structured.

\- The current version does not provide a web interface or save results automatically.



\## 9. Conclusion



The Meeting to Scope agent successfully converts sample meeting notes into structured project scope information. All three automated tests passed.

