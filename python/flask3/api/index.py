from flask import Flask

data = 0
app = Flask(__name__)

@app.route("/get")
def get():
    return str(data)

@app.route("/set")
def set():
    data += 1
    return "Done"

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
