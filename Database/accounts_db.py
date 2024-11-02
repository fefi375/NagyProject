import sqlite3

# csatlakozás az adatbázishoz vagy létrehozás ha nem létezik
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()