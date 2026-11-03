

\# Community Content Moderation System



A lightweight content moderation system built with Python and FastAPI.



\## 1. Project Overview



This project implements a rule-based content moderation system

for identifying potentially risky user-generated content.



It supports keyword detection, phone number recognition,

external link detection, risk scoring and batch moderation.



\## 2. Key Features



\- Advertisement and spam detection

\- Inappropriate language detection

\- Phone number recognition

\- External URL detection

\- Risk scoring and classification

\- RESTful API with FastAPI

\- CSV batch content moderation

\- Automated testing with unittest



\## 3. Technology Stack



\- Python

\- FastAPI

\- Uvicorn

\- Regular Expressions

\- CSV

\- unittest



\## 4. Project Structure



```text

community-content-moderation/

├── app/

│   ├── rules.py

│   ├── moderation.py

│   ├── batch\_moderation.py

│   └── main.py

├── tests/

│   ├── test\_moderation.py

│   ├── test\_api.py

│   └── test\_batch\_moderation.py

├── data/

│   └── sample\_comments.csv

├── docs/

├── README.md

├── requirements.txt

└── .gitignore

```



\## 5. Installation



Install dependencies:



```bash

pip install -r requirements.txt

```



\## 6. Run the API



```bash

python -m uvicorn app.main:app --reload

```



Open the API documentation:



http://127.0.0.1:8000/docs



\## 7. Batch Moderation



```bash

python -m app.batch\_moderation

```



\## 8. Run Tests



```bash

python -m unittest discover -s tests -v

```



Current test result: 14 tests passed.



\## 9. Limitations



This project uses predefined rules and regular expressions.

It is an educational prototype, not a production-grade

AI moderation system.



Its rules do not represent the actual moderation policies

of any social media platform.



