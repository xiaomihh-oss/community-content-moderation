# Community Content Moderation System

A lightweight rule-based content moderation system built with Python and FastAPI.

## 1. Project Overview

This project aims to identify potentially risky user-generated content through predefined rules and text pattern matching.

It provides content detection, risk scoring, RESTful API services, and CSV-based batch moderation.

## 2. Key Features

- **Keyword Detection:** Identify potential advertisements, spam, and inappropriate language.
- **Pattern Recognition:** Detect phone numbers and external URLs using regular expressions.
- **Risk Assessment:** Calculate risk scores and classify content into low, medium, and high-risk levels.
- **RESTful API:** Provide content moderation services through FastAPI.
- **Batch Processing:** Support CSV-based batch content moderation and report generation.
- **Automated Testing:** Validate moderation rules, API endpoints, and batch processing.

## 3. Technology Stack

| Technology | Application |
|---|---|
| Python | Core development |
| FastAPI | Backend API |
| Uvicorn | API server |
| Regular Expressions | Text pattern detection |
| CSV | Batch data processing |
| unittest | Automated testing |

## 4. System Architecture

```text
User Input / CSV Data
        |
        v
Content Moderation Engine
        |
        v
Rule-based Detection
  - Keyword Detection
  - Phone Number Detection
  - URL Detection
        |
        v
Risk Scoring
        |
        v
Risk Classification
        |
        v
Moderation Results
        |
        v
API Response / CSV Report
```

## 5. Project Structure

```text
community-content-moderation/
├── app/
│   ├── rules.py
│   ├── moderation.py
│   ├── main.py
│   └── batch_moderation.py
├── tests/
│   ├── test_moderation.py
│   ├── test_api.py
│   └── test_batch_moderation.py
├── data/
│   └── sample_comments.csv
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

## 6. Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. Run the API

```bash
python -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## 8. Run Batch Moderation

```bash
python -m app.batch_moderation
```

The system generates a CSV file containing moderation results and a summary report.

## 9. Automated Testing

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

**Current test results: 14 tests passed.**

Test coverage includes:

- Content detection rules
- API endpoint validation
- Batch CSV processing
- Invalid input handling

## 10. Limitations

This project currently uses predefined rules and regular expressions rather than machine learning models.

It is an educational prototype and does not represent the actual moderation policies or production systems of any social media platform.
