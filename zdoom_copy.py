from flask import Flask, render_template, request, Response, current_app, g, flash
import sqlite3
from faker import Faker
import pandas as pd
from datetime import datetime
import click

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hshshsh ehehhe'
#Initialize Faker
fake = Faker(['en_US'])

def insert_user(user, password):
    with sqlite3.connect('mydatabase.db') as connection:
        #create a cursor object
        cursor = connection.cursor()
        user_data = (user, password)
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );'''

        # Execute the SQL command
        cursor.execute(create_table_query)
      #  cursor.execute(insert_query, student_data)
        user_exists = cursor.execute("SELECT * FROM Users WHERE name = ?", (user,)).fetchall()
        if user_exists:
            print("Error, try a different name")
            app.logger.error('User {} already exists'.format(user))
        else:
            cursor.execute("""
            INSERT INTO Users (name, password) 
            VALUES (?, ?)
            """, user_data)
            app.logger.info('User {} was successfully added'.format(user))
        # Commit the changes
        connection.commit()
        print('connected to database successfully')

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        insert_user(username, password)
        return "We think we can add you in our database"
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
    app.run(debug=True)