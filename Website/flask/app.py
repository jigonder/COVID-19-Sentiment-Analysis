from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)


mongo = PyMongo(app, uri = "mongodb://localhost:27017/project_0")

@app.route("/")
def index():
    data = mongo.db.collection.find()
    return render_template("index.html", data=data)

@app.route("/page_1")
def page_1():
    return render_template("page_1.html")

@app.route("/page_2")
def page_2():
    return render_template("page_2.html")

@app.route("/page_3")
def page_3():
    return render_template("page_3.html")

@app.route("/home")
def mainpage():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    