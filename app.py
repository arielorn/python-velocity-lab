from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    sentence = Markup(f"Hello, {name}!<br>Welcome to Velocity.")
    return render_template('hello.html', sentence=sentence)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
