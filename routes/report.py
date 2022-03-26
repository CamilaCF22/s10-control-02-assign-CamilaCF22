from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from utils.bcryptService import bcrypt
from models.user import User
from utils.db import db

report = Blueprint("report", __name__)


@report.route("/")
def home():
    return render_template("report/home.html")