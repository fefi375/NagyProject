from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # ide kell sajat tikos kulcs

# adatbázishoz kapcsolódódáshoz segítő funkció
def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn