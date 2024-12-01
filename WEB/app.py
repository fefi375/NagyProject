from flask import Flask, request, redirect, render_template, url_for, flash, session
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home
@app.route('/')
def home():
    return render_template('homepage.html')

#Regisztráció
@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert new user into the database with default credit of 500
        cursor.execute('INSERT INTO users (username, password, credit) VALUES (?, ?, ?)', (username, password, 500))
        conn.commit()
        flash("Account created successfully! Please log in.")
    except sqlite3.IntegrityError:
        flash("Username already taken. Please choose another.")
    finally:
        conn.close()

    return redirect(url_for('home'))

# Bejelentkezés
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

#bannolt fiók
@app.route('/banned_account')
def banned_account_page():
    return render_template('banned_account.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',  (username, password))
    user = cursor.fetchone()
    conn.close()

    if user['credit']<=50:
        return redirect(url_for('banned_account_page'))
    if user:
        session['user_id'] = user['id']
        session['username'] = user['username']
        flash(f"Welcome back, {user['username']}! Your current credit is {user['credit']}.")
        return redirect(url_for('news_portal'))
        
    else:
        flash("Invalid username or password. Please try again.")
        return redirect(url_for('login_page'))
    
    


# fiók létrehozása
@app.route('/account_create', methods=['GET'])
def create_account_page():
    return render_template('account_create.html')


# kijelentkezés
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('home'))

# hírportál főoldala
@app.route('/news_portal')
def news_portal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    conn.close()
    return render_template('news_portal.html', articles=articles)

# egyes cikkekhez vezető út
@app.route('/article/<int:article_id>')
def article(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    article = cursor.fetchone()
    conn.close()
    if article:
        return render_template('article.html', article=article)
    else:
        flash("Article not found.")
        return redirect(url_for('news_portal'))



# Cenzúra lista betöltése
def load_censor_list(filename='censor_list.txt'):

    censor_data = {}
    with open(filename, 'r', encoding='utf-8') as f:  # UTF-8 kódolás beállítása
        for line in f:
            bad_word, good_word, credit_cost = line.strip().split(' : ')
            censor_data[bad_word.lower()] = (good_word, int(credit_cost))  # Convert bad_word to lowercase for consistency
    return censor_data

# Cenzúrázó funkció
def censor_content(content, censor_data):
    adjusted_content = content
    total_social_credit_adjustment = 0

    for bad_word, (good_word, credit_cost) in censor_data.items():
        # Count occurrences of the bad word (case insensitive)
        occurrences = len(re.findall(r'\b' + re.escape(bad_word) + r'\b', adjusted_content, flags=re.IGNORECASE))
        
        # Replace bad word with good word (case insensitive)
        adjusted_content = re.sub(r'\b' + re.escape(bad_word) + r'\b', good_word, adjusted_content, flags=re.IGNORECASE)
        
        # Calculate social credit adjustment
        total_social_credit_adjustment -= occurrences * credit_cost

    return adjusted_content, total_social_credit_adjustment

# Új cikk feltöltése
@app.route('/upload_article', methods=['GET', 'POST'])
def upload_article():
    if 'user_id' not in session:
        flash("Please log in to upload an article.")
        return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_id = session['user_id']

        # Load censor data
        censor_data = load_censor_list()

        # Censor title and content
        censored_title, title_credit_adjustment = censor_content(title, censor_data)
        censored_content, content_credit_adjustment = censor_content(content, censor_data)

        # Calculate total credit adjustment
        total_credit_adjustment = title_credit_adjustment + content_credit_adjustment

        # Connect to the database and save the article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id) VALUES (?, ?, ?)', (censored_title, censored_content, author_id))

        # Update user's credit score
        cursor.execute('UPDATE users SET credit = credit + ? WHERE id = ?', (total_credit_adjustment, author_id))
        conn.commit()
        conn.close()

        
        flash("Article uploaded successfully with censorship applied!")
        return redirect(url_for('news_portal'))
        
    return render_template('upload_article.html')


if __name__ == '__main__':
    app.run(debug=True)
