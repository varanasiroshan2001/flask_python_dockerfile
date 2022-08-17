#app.py
from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/time")
def time():
    datetime1=dt.now()
    return str(datetime1)