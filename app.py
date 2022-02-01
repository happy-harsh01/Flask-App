from flask import Flask, render_template, url_for ,requests, redirect 
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Datetime, default = datetime.utcnow)

    def __repr__(self):
        return "<Task%r>"%self.id

app.route('/', methods = ['POST', 'GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
