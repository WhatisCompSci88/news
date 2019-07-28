from app import app
from flask import flash, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
import os

# STARTING PAGE
@app.route("/")
def welcome():
    if "username" in session:
        return redirect(url_for("stocks"))
    return render_template("welcome.html")

# AUTHENTICATION
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/register/auth", methods=["POST"]) ##
def register_auth():
    pass

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/login/auth", methods=["POST"]) ##
def login_auth():
    pass

@app.route("/logout", methods=["GET"])
def logout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("welcome"))

# STOCK RELATED
# Lists all stocks that you want tracked (possibly through a Materialize card?)
@app.route("/stocks", methods=["GET"]) ##
def stocks():
    pass

# Displays search bar
@app.route("/stocks/search", methods=["GET", "POST"]) ##
def search_stock():
    pass

# Adds stock to tracker
@app.route("/stocks/add") ##
def add_stock():
    pass

# Views a specific stock
@app.route("stocks/view") ##
def view_stock():
    pass
