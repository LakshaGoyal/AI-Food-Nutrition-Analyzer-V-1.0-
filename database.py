import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'meals.db')

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            food_item TEXT NOT NULL,
            calories REAL NOT NULL,
            protein REAL NOT NULL,
            carbs REAL NOT NULL,
            fat REAL NOT NULL,
            image_filename TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS steps (
            date TEXT PRIMARY KEY,
            steps INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_meal(date, food_item, calories, protein, carbs, fat, image_filename):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO meals (date, food_item, calories, protein, carbs, fat, image_filename)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, food_item, calories, protein, carbs, fat, image_filename))
    conn.commit()
    conn.close()

def get_meals_by_date(date):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM meals WHERE date = ?', (date,))
    meals = [dict(row) for row in c.fetchall()]
    conn.close()
    return meals

def get_all_meals():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM meals ORDER BY date DESC')
    meals = [dict(row) for row in c.fetchall()]
    conn.close()
    return meals

def log_steps(date, steps):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO steps (date, steps)
        VALUES (?, ?)
    ''', (date, steps))
    conn.commit()
    conn.close()

def get_steps(date):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT steps FROM steps WHERE date = ?', (date,))
    row = c.fetchone()
    conn.close()
    if row:
        return row[0]
    return 0

# Initialize DB on load
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
init_db()
