# app.py
from flask import Flask, request

app = Flask(__name__)

# HTML template for the index page
INDEX_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Velocity Tech</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        img {
            max-width: 200px;  /* Adjust the size as needed */
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="/static/velocity-tech-logo.png" alt="Velocity Tech Logo">
        <h1>Welcome to Velocity Tech</h1>
        <form method="post" action="/hello">
            <label for="name">Enter your name:</label><br>
            <input type="text" id="name" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
'''

# HTML template for the hello page

HELLO_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        img {
            max-width: 200px;  /* Adjust the size as needed */
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="/static/velocity-tech-logo.png" alt="Velocity Tech Logo">
        <h1>Hello, {name}!</h1>
    </div>
</body>
</html>
'''
@app.route('/')
def index():
    return INDEX_HTML

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return HELLO_HTML.replace('{name}', name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)