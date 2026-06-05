from flask import Flask, render_template, request, Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hshshsh ehehhe'
@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        username = request.form['username']
        return f"hello {username}"
    return render_template('index.html')

@app.route('/theories')
def theory():
    return render_template('ex_avp.html')


if __name__ == '__main__':
    app.run(debug=True)