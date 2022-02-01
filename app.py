from flask import Flask, render_template, url_for ,requests, redirect 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///test.db'

app.route('/', methods = ['POST', 'GET'])
def index():
    return "Hello World"
