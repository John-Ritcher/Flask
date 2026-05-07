from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/actor')
def actor():
    return render_template('actor.html')