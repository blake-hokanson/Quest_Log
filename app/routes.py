from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game/<id>")
def game(id):
    return render_template("game.html", id=id)

@app.route("/profile/<id>")
def profile(id):
    return render_template("profile.html", id=id)

@app.route("/register")
def register():
    return "<p>Register</p>"

@app.route("/login")
def login():
    return "<p>Login</p>"