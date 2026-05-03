import pandas as pd
import sqlite3, os

# 1. load scraped CSV ---
input_file = "data/processed/books.csv"
df = pd.read_csv(input_file)
print(f"Loaded {len(df)} rows from {input_file}")

# --- 2. clean text fields ---
df["title"] = (
    df["title"]
    .str.lower()      # lowercase
    .str.strip()      # remove leading / trailing space
)

# Optional: remove punctuation (uncomment if need be)
# df["title"] = df["title"].str.replace(r"[^\w\s]", "", regex=True)

# 3. save cleaned CSV ---
os.makedirs("data/processed", exist_ok=True)
clean_file = "data/processed/books_clean.csv"
df.to_csv(clean_file, index=False)
print(f"Saved cleaned dataset to {clean_file}")

# 4. store in SQLite ---
os.makedirs("data", exist_ok=True)
db_file = "data/books.db"
conn = sqlite3.connect(db_file)
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()
print(f"Stored cleaned dataset in SQLite: {db_file}")

# 5. verify by reading from DB ---
conn = sqlite3.connect(db_file)
check = pd.read_sql("SELECT * FROM books LIMIT 5;", conn)
conn.close()

print("🔍 Preview from SQLite:")
print(check)
