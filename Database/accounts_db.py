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
    credit REAL DEFAULT 0
)
''')

# commitolás és kapcsolat lezárása
conn.commit()
conn.close()

print("Database and table created successfully!")