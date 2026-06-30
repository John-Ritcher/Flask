from flask import Flask, redirect, render_template, request, Response, current_app, g, flash, session, url_for
import sqlite3
from faker import Faker
from zoneinfo import ZoneInfo
import pandas as pd
import datetime as dt
import click
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hshshsh ehehhe'
#Initialize Faker
fake = Faker(['en_US'])

def create_table():
    with sqlite3.connect('mydatabase.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """)

# @app.route('/signup', methods=['POST'])
def insert_user(user, password):
    with sqlite3.connect('mydatabase.db') as connection:
        #create a cursor object
        cursor = connection.cursor()
        user_data = (user, password)

        # Execute the SQL command
      #  cursor.execute(insert_query, student_data)
        user_exists = cursor.execute("SELECT * FROM Users WHERE name = ?", (user,)).fetchone()
        if user_exists:
            print("Error, try a different name")
            #current_app.logger.error('User {} already exists'.format(user))
            flash('Username already exists', 'error')
        else:
            cursor.execute("""
            INSERT INTO Users (name, password) 
            VALUES (?, ?)
            """, user_data)
            user_login = cursor.execute("SELECT * FROM Users WHERE name = ?", (user,)).fetchone()
            session['user_id'] = user_login[0]
            #current_app.logger.info('User {} was successfully added'.format(user))
            flash('User created', 'success')
        # Commit the changes
        connection.commit()
        print('connected to database successfully')

def login_user(user, password):
    with sqlite3.connect('mydatabase.db') as connection:
        cursor = connection.cursor()
        error = None

        user_login = cursor.execute("SELECT * FROM Users WHERE name = ?", (user,)).fetchone()
        if user_login is None:
            error = "Invalid username"
        elif not check_password_hash(user_login[2], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user_login[0]
            print(session['user_id'])
            flash('Logged in', 'success')
        else:
            flash(error)

def load_logged_user():
    with sqlite3.connect('mydatabase.db') as connection:
        cursor = connection.cursor()
        user_id = session.get('user_id')
        if user_id is None:
            #print("Logged user not logged in")
            flash('Logged user not logged in', 'error')
        else:
            cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,)).fetchone()
            #print("logged user")
            flash("Logged user", "success")

def insert_comment(comment):
    with sqlite3.connect('mydatabase.db') as connection:
        cursor = connection.cursor()
        user_id = session.get('user_id')
        user_comment = (user_id, comment)
        if user_id is None:
            print("Logged user not logged in (from insert_comment)")
        else:
            cursor.execute("""
            INSERT INTO Comments (user_id, content)
            VALUES (?, ?)
            """, user_comment)

def get_comments():
    with sqlite3.connect('mydatabase.db') as connection:
        cursor = connection.cursor()

        comments = cursor.execute("""
        SELECT 
            Users.name,
            Comments.content,
            Comments.created_at
        FROM Comments
        JOIN Users
        ON  Users.id = Comments.user_id
        ORDER BY Comments.created_at DESC
        """)

        return format_time(comments)

def format_time(comments):
    comments = comments.fetchall()
    formatted_comments = []

    for comment in comments:
        data = dt.datetime.fromisoformat(comment[2])
        now = dt.datetime.now()

        delta = now - data
        years = delta.days // 365
        months = delta.days // 30
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        if delta.days > 365:
            if delta.days > 730:
                time = f"{years} years ago"
            else:
                time = f"{years} year ago"
        elif months > 0:
            if months > 1:
                time = f"{months} months ago"
            else:
                time = f"{months} month ago"
        elif delta.days > 0:
            if delta.days > 1:
                time = f"{delta.days} days ago"
            else:
                time = f"{delta.days} day ago"
        elif hours > 0:
            time = f"{hours} hours ago"
        elif minutes > 0:
            time = f"{minutes} minutes ago"
        elif delta.seconds > 0 > minutes:
            time = f"{delta.seconds} seconds ago"

        formatted_comments.append({'name': comment[0], 'content': comment[1], 'time': time})

    return formatted_comments

@app.route('/', methods=['GET', 'POST'])
def root():
    load_logged_user()
    comments = get_comments()
    if request.method == 'POST':
        action = request.form['action']
        if action == 'signup':
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '').strip()
            if len(username) < 2:
                flash('Username must be at least 2 characters', 'error')
            elif len(password) < 8:
                flash('Password must be at least 8 characters', 'error')
            else:
                password_hash = generate_password_hash(password)
                insert_user(username, password_hash)
        elif action == 'login':
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '').strip()
            if len(username) < 2:
                flash('Username must be at least 2 characters', 'error')
            elif len(password) < 8:
                flash('Password must be at least 8 characters', 'error')
            else:
                login_user(username, password)
        elif action == 'logout':
            session.clear()
            flash('Logged out', 'success')
        elif action == 'comment':
            comment = request.form.get('comment', '').strip()
            insert_comment(comment)
    print(dict(session))
    return render_template('index.html', comments=comments)

@app.route('/theories')
def theory():
    return render_template('ex_avp.html')


'''def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

sqlite3.register_converter('timestamp', lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)'''

if __name__ == '__main__':
    create_table()
    app.run(debug=True)