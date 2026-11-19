from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/name')
def give_name():
    return "<p> João Felipe</p>"

@app.route("/age")
def give_age():
    age = datetime.now().year - 2008
    return f"<p> {age} years old</p>"

@app.route("/sport")
def give_sport():
    return "<p> Swimming Ski</p>"
