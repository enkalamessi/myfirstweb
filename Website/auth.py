from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return "<button>Login</button>"


@auth.route("/logout")
def lougout():
    return "<p>Logout</p>"


auth.route("/signup")
def sign_up():
    return "<p>Sign Up</p>"
