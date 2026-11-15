import csv
import sqlite3
from pathlib import Path

DATABASE_NAME = Path(__file__).parent / "herrights.db"
CSV_FILE = Path(__file__).parent / "data" / "legal_rights.csv"

def create_database():
    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS legal_rights (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                law TEXT NOT NULL,
                description TEXT NOT NULL,
                keywords TEXT,
                recommended_actions TEXT,
                possible_remedies TEXT,
                urgency TEXT,
                source_url TEXT,
                review_notes TEXT
            )
        """)

def import_legal_data():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"CSV file not found: {CSV_FILE}")
    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        with sqlite3.connect(DATABASE_NAME) as connection:
            for row in reader:
                connection.execute("""
                    INSERT OR REPLACE INTO legal_rights
                    (id, category, title, law, description, keywords, 
                    recommended_actions, possible_remedies, urgency, 
                    source_url, review_notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    row["id"],
                    row["category"],
                    row["title"],
                    row["law"],
                    row["description"],
                    row["keywords"],
                    row["recommended_actions"],
                    row["possible_remedies"],
                    row["urgency"],
                    row["source_url"],
                    row["review_notes"]
                ))

def get_rights_by_category(category):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.execute("""
            SELECT title, description, law, source_url
            FROM legal_rights
            WHERE category = ?
            ORDER BY title
        """, (category,))

    rights = cursor.fetchall()
    return rights