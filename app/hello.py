from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)



@app.route('/')
def index():
	# return 'Index Page'
	return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'