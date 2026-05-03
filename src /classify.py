import os, json, time, joblib, sqlite3
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report
import random
import numpy as np

 # Set deterministic global seeds for reproducible results
random.seed(42)
np.random.seed(42)

# --- 1. Load data ---
# Option A: from CSV
df = pd.read_csv("data/processed/books_clean.csv")

# Option B (alternative): from SQLite
# conn = sqlite3.connect("data/books.db")
# df = pd.read_sql("SELECT * FROM books;", conn)
# conn.close()

print(f"Loaded {len(df)} rows for classification")

# --- 2. Split data ---
X_train, X_test, y_train, y_test = train_test_split(
    df["title"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# --- 3. Vectorize text (TF-IDF) ---
vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

# --- 4. Train model (Logistic Regression) ---
clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train_vec, y_train)

# --- 5. Evaluate model ---
y_pred = clf.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="macro")

print(f"\nAccuracy: {acc:.3f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# --- 6. Save metrics ---
os.makedirs("logs", exist_ok=True)
pd.DataFrame([{"accuracy": acc, "f1_macro": f1}]).to_csv("logs/metrics.csv", index=False)
print("Metrics saved to logs/metrics.csv")

# --- 7. Save model + vectorizer ---
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/model.pkl")
joblib.dump(vec, "models/vectorizer.pkl")
print("Model and vectorizer saved in 'models/'")

# --- 8. Save JSON summary (for reproducibility) ---
metrics = {
    "task": "classification",
    "accuracy": float(acc),
    "f1_macro": float(f1),
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "model_file": "model.pkl",
    "vectorizer_file": "vectorizer.pkl",
}
with open("models/metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)
print("metrics.json saved in 'models/'")
