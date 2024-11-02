import sqlite3

# csatlakozás az adatbázishoz vagy létrehozás ha nem létezik
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Felhasználói tábla létrehozása
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    credit REAL DEFAULT 500
)
''')

# cikk táblázat létrehozása
cursor.execute('''
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES users(id)
)
''')


# commitolás és kapcsolat lezárása
conn.commit()
conn.close()

print("Database and table created successfully!")