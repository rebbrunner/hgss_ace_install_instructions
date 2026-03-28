from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/platinum')
def platinum():
    return '<p>platinum link</p>'

@app.route('/hgss')
def hgss():
    return '<p>hgss</p>'
