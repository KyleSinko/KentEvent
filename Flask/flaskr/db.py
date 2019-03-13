from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{lou0891}:{engineering}@{lou0891.mysql.pythonanywhere-services.com}/{lou0891$default}".format(
    username="lou0891",
    password="engineering",
    hostname="lou0891.mysql.pythonanywhere-services.com",
    databasename="lou0891$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ID model, getting IDs from ID table
class ID(db.Model):

    __tablename__ = "ID"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))