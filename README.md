# ML Reproducible Systems

End-to-end reproducible ML pipeline — from data scraping to a Dockerized FastAPI inference endpoint with a Streamlit UI, automated with Makefile and GitHub Actions CI.

---

## Overview

A text classification system that scrapes book data, trains a genre classifier, and serves predictions through a REST API — built with reproducibility as a core requirement: pinned dependencies, fixed random seeds, automated testing, and containerized deployment.

---

## Demo

![Streamlit UI](https://github.com/user-attachments/assets/77c726f0-2cd2-4eda-9e8f-3ec139cd5655)

---

## Pipeline

```
fetch_data → scrape → clean → train classifier → FastAPI endpoint → Streamlit UI
```

All steps automated via `make all`.

---

## Results

Book genre classification (text → label):

```bash
$ curl -X POST "http://localhost:8000/predict" -d '{"text": "the grand design"}'
"science"
```

---

## Quick Start

```bash
# Install dependencies, run tests, run full pipeline
make all

# Start API
make run-api
# → http://localhost:8000

# Start Streamlit UI
make run-streamlit
# → http://localhost:8501
```

**Or run via Docker:**

```bash
docker build -t myapi .
docker run -p 8000:8000 myapi
```

---

## Repo Structure

```
├── .github/workflows/
│   └── ci.yml              # GitHub Actions CI
├── src/
│   ├── fetch_data.py       # Raw HTML fetching
│   ├── scrape_books.py     # HTML → CSV parsing
│   ├── clean_books.py      # Text cleaning
│   ├── classify.py         # Model training & evaluation
│   ├── api.py              # FastAPI inference endpoint
│   ├── app.py              # Streamlit frontend
│   └── processor.py        # Data processing utilities
├── tests/
│   ├── test_processor.py   # Unit tests
│   └── test_smoke.py       # Smoke tests
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

---

## Tech Stack

Python 3.11 · FastAPI · Streamlit · Docker · GitHub Actions CI · pytest · Makefile · BeautifulSoup · scikit-learn
