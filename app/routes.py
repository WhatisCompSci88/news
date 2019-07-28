from app import app
from flask import flash, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
import os

@app.route("/")
def welcome():
    pass
