\# Task 2: Inbox Agent Documentation



\## 1. Project Overview



The Inbox Agent is a Python-based email analysis tool. It identifies email priority, categorizes messages, and generates suggested replies.



\## 2. Technologies Used



\- Python 3

\- Python unittest testing framework

\- Datetime module



\## 3. Features



\### Email Priority Detection



The agent identifies urgent emails using keywords such as:

\- urgent

\- ASAP

\- immediately

\- deadline



Emails containing these keywords are marked as high priority. Other emails are marked as normal priority.



\### Email Categorization



The agent classifies emails into the following categories:



\- \*\*Billing:\*\* invoice, payment, billing, refund

\- \*\*Meeting:\*\* meeting, schedule, calendar

\- \*\*Support:\*\* issue, problem, error, help

\- \*\*General:\*\* emails that do not match the other categories



\### Suggested Reply Generation



The agent generates a suggested reply acknowledging the sender's message. The reply is a draft and is not automatically sent.



\### Email Information



The analysis output includes:

\- Subject

\- Sender

\- Priority

\- Category

\- Analysis timestamp

\- Suggested reply



\## 4. Project Structure



```text

task2/

├── src/

│   └── inbox\_agent.py

├── tests/

│   └── test\_inbox\_agent.py

└── docs/

&#x20;   └── INBOX\_AGENT\_DOCUMENTATION.md

```



\## 5. How to Run



From the `task2` directory, run:



```powershell

python .\\src\\inbox\_agent.py

```



The program analyzes a sample email and prints the results.



\## 6. How to Run Tests



Run:



```powershell

python -m unittest discover -s tests -v

```



\## 7. Testing Results



Three automated tests have passed:



| Test | Expected Result | Status |

|---|---|---|

| Urgent meeting email | High priority, meeting category | PASS |

| Billing email | Billing category | PASS |

| General email | Normal priority, general category | PASS |



\*\*Total tests passed:\*\* 3



\## 8. Current Limitations



\- The agent currently analyzes sample email data rather than connecting to a real inbox.

\- Classification uses keyword matching rather than a trained AI model.

\- Suggested replies require human review before sending.



\## 9. Conclusion



The Inbox Agent successfully demonstrates basic email prioritization, categorization, and suggested reply generation. Automated tests verify the core functionality.

