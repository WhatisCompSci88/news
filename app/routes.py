import os
from app import app
from flask import flash, render_template, request, redirect, url_for, session
from app.models import apiUtils
from app.models import newsUtils
from flask_pymongo import PyMongo

app.secret_key = os.urandom(32)
# STARTING PAGE
@app.route("/")
# NEWS API KEY: 12126d1b282e4c94a45c9a108b94f246
def start():
    if not "username" in session:
        return redirect(url_for("news"))
    else:
        return redirect(url_for("home"))

# NAVBAR OPTIONS
@app.route("/home")
def home():
    if not "username" in session:
        return redirect(url_for("login"))
    else:
        return render_template("home.html")

@app.route("/news")
def news():
    logged = "username" in session
    sitesList = newsUtils.getSiteList(10)
    articlesList = []
    for site in sitesList:
        siteId = apiUtils.idDict[site]
        article = apiUtils.getTopResponse(siteId)
        articlesList.append(article)
        for key in article:
            print(key, "/", article[key])
        print("\n")
    return render_template("news.html", articlesList=articlesList, logged=logged)


@app.route("/finance")
def finance():
    logged = "username" in session
    return render_template("finance.html", logged=logged)
    
@app.route("/about")
def about():
    logged = "username" in session
    return render_template("about.html", logged=logged)
    
# SEARCH REQUESTS
@app.route("/search/news")
def searchNews():
    logged = "username" in session
    return render_template("search.html", category="news")
    
@app.route("/search/finance")
def searchFinance():
    logged = "username" in session
    return render_template("search.html", category="finance")

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
    
# SAVE REQUESTS
@app.route("/save/article", methods=["POST"])
def saveArticle():
    pass
    
@app.route("/save/stock", methods=["POST"])
def saveStock():
    pass