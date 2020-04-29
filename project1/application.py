from flask import Flask, render_template, url_for,redirect, flash
from forms import RegistrationForm, LoginForm
import requests
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rbkoemzpycogam:383c68f0a2c2b051f6b9ae8778f41d1a09247725325e4027fa82335a756671b5@ec2-79-125-26-232.eu-west-1.compute.amazonaws.com:5432/dehvr9dets08v9"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods = ["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        fullname = form.fullname.data
        enc_pass = hashlib.sha512(password.encode())
        flash("Register completed","success")
        return redirect(url_for("/login"))

    return render_template("register.html", form = form)

@app.route("/login", methods = ["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return redirect(url_for("home_user", username = username))

    return  render_template("login.html", form = form)

@app.route("/home/<string:username>", methods = ["POST","GET"])
def home_user(username):
    return render_template("login_home.html")




if __name__ == "__main__":
    app.run(debug= True)