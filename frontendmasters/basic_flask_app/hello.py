from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    name = "ikram"
    return render_template("index.html", name=name)

@app.route("/french")
def bonjour():
    return "Bonjour World!"

@app.route("/name/<name>")
def hello_name(name):
    return f"hello, {name}"

#? FLASK_APP=hello.py FLASK_ENV=development python3 -m flask run 