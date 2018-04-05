from flask import Flask, render_template, url_for, redirect
from flask_bower import Bower

app = Flask(__name__)
Bower(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error(errnum=404):
    return "Sorry, there was an error - {}".format(errnum)

app.run(debug=True, port=9000, host='localhost') #debug=True enables reload while developing
