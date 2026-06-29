from flask import Blueprint, render_template, request, redirect
from app.models import User
from app.extensions import db, bcrypt
from flask_login import login_user, logout_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        hashed = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")

        user = User(
            username=request.form["username"],
            password=hashed,
            role="user"
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect("/")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/login")