from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://todo.sqlite'
db = SQLAlchemy(app)

class List(db.Model):

    __tablename__ = "lists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text())
    category = db.Column(db.Text())
    description = db.Column(db.Text())


if __name__ == "__main__":
    pass


