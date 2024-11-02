from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # ide kell sajat tikos kulcs

# adatbázishoz kapcsolódódáshoz segítő funkció
def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# A főoldalra vezető út
@app.route('/')
def home():
    return render_template('index.html')

# fiók létrehozását kezelő oldal
@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # új felhasználó létrehozása 500 credittel
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        flash("Account created successfully!")
    except sqlite3.IntegrityError:
        flash("Username already taken. Please choose another.")
    finally:
        conn.close()

    return redirect(url_for('home'))


# Bejelentkezetető oldal kezelése
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        flash(f"Welcome back, {username}! Your current credit is {user['credit']}.")
    else:
        flash("Invalid username or password. Please try again.")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)