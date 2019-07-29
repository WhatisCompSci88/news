from app import app

from flask import flash, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo

import os

from app.models import news

# STARTING PAGE
@app.route("/")
def welcome():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("welcome.html")

# NEWS API KEY: 12126d1b282e4c94a45c9a108b94f246

# NEWS RELATED
@app.route("/")
def home():
    sites = news.getSiteList(10)
    return render_template("home.html", sites)




'''
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
@app.route("/news/stocks", methods=["GET"]) ##
def stocks():
    return render_template("stocks.html")

# Displays searched stock
@app.route("/news/stocks/search", methods=["GET"]) ##
def search_results():
    return render_template("search_results.html")

# Adds stock to tracker
@app.route("/news/stocks/add", methods=["GET"]) ##
def add_stock():
    pass

# Views a specific stock
@app.route("/news/stocks/view", methods=["GET"]) ##
def view_stock():
    return render_template("view_stock.html")
'''