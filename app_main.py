from flask import Flask, redirect, render_template, request, Response, current_app, g, flash, session, url_for
import sqlite3
from faker import Faker
import pandas as pd
from datetime import datetime
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
            print("Logged user not logged in")
            #flash('Logged user not logged in', 'error')
        else:
            cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,)).fetchone()
            print("logged user")
            #flash("Logged user", "success")
@app.route('/', methods=['GET', 'POST'])
def root():
    load_logged_user()
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
    print(dict(session))
    return render_template('index.html')

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