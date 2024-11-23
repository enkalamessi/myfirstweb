from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route("/logout")
def lougout():
    return "<p>Logout</p>"


auth.route("/signup")
def sign_up():
    return "<p>Sign Up</p>"
