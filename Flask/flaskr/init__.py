from flask import Flask, render_template  #starts flaskproject 
from flask_bootstrap import Bootstrap   #For framework
from flask_scss import SCSS 

app = Flask(__name__)
Bootstrap(app)

@app.route("/")    #Routes 
def renderLanding():
    return render_template("landing.html")  #Function that renders them 

@app.route("/login")
def renderLogin():
    return render_template("login/login.html")

@app.route("/login/forgot")
def renderForgotPassword():
    return render_template("login/forgot.html")

@app.route("/register")
def renderRegister():
    return render_template("register/register.html")

@app.route("/profile")
def renderProfile():
    return render_template("profile/profile.html")

@app.route("/profile/myevents")
def renderMyEvents():
    return render_template("profile/myevents.html")

@app.route("/events")
def renderEvents():
    return render_template("events/events.html")  

@app.route("/settings")
def renderSettings():
    return render_template("settings/settings.html")
