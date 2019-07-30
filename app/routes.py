import os
from app import app
from flask import flash, render_template, request, redirect, url_for, session
from app.models import newsUtils, stocksUtils
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = "final_project_test"
app.config['MONGO_URI'] = "mongodb+srv://admin:nZ0ELdTyXc6f5utn@cluster0-wb3wx.mongodb.net/final_project_test?retryWrites=true&w=majority"
mongo = PyMongo(app)

def addUser(username, password):
    collection = mongo.db.user_database
    users = list(collection.find({}))
    userId = len(users) + 1
    collection.insert({
        "userId": userId,
        "username": username,
        "password": password,
        "savedArticles": {},
        "savedStocks": []
    })
    return userId

def getUserData(username):
    collection = mongo.db.user_database
    users = list(collection.find({"username":username}))
    if len(users) == 0:
        return -1
    else:
        return users[0]

def getUserId(username):
    collection = mongo.db.user_database
    users = list(collection.find({"username":username}))
    if len(users) == 0:
        return -1
    else:
        return users[0]["userId"]

def authenticateUser(username, password):
    user = getUserData(username)
    if user["username"] == username and user["password"] == password:
        return True
    else:
        return False


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
        return render_template("home.html", logged = True)

@app.route("/news")
def news():
    logged = "username" in session
    sitesList = newsUtils.getSiteList(10)
    articlesList = []
    for site in sitesList:
        siteId = newsUtils.idDict[site]
        article = newsUtils.getTopResponse(siteId, articlesList)
        articlesList.append(article)
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
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        if getUserId(username) == -1:
            if password == confirm:
                addUser(username, password)
                flash("ACCOUNT SUCCESSFULLY CREATED")
            else:
                flash("PASSWORDS DO NOT MATCH")
        else:
            flash("USERNAME TAKEN")
    return redirect(url_for("register"))
    

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/login/auth", methods=["POST"]) ##
def login_auth():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticateUser(username, password):
            session["username"] = username
            return redirect(url_for("home"))
        else:
            flash("INCORRECT USERNAME OR PASSWORD")
    return redirect(url_for("login"))

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