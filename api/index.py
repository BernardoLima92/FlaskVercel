from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Valeu ai Gileadeeeeeeeeeeee!'

@app.route('/about')
def about():
    return 'texto'