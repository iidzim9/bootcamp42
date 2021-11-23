from flask import Flask, app
a = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"