from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)



@app.route('/')
def index():
	# return 'Index Page'
	return render_template('girl.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/donate')
def donate():
	return render_template('donation.html')

