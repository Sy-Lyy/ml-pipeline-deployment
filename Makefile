.PHONY: install test get-data scrape clean train all run-api run-streamlit 

# 1. Install dependencies
install:
	pip install -r requirements.txt

# 2. Run pytest (Week 3)
test:
	pytest -q

# 3. Data collection, scraping, cleaning, train and classify (Week 5)

get-data:
	python src/fetch_data.py

scrape:
	python src/scrape_books.py

clean:
	python src/clean_books.py

train:
	python src/classify.py

# 4. Run API server and Streamlit app (Week 6)

run-api:
	.venv\Scripts\python -m uvicorn src.api:app --reload --port 8000

run-streamlit:
	streamlit run src/app.py

all: install test get-data scrape clean train
