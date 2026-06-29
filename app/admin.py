from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from app.models import Exercise
from app.extensions import db

admin_bp = Blueprint("admin", __name__)

def is_admin():
    return current_user.role == "admin"


@admin_bp.route("/admin")
@login_required
def admin():

    if not is_admin():
        return "No autorizado"

    exercises = Exercise.query.all()
    return render_template("admin.html", exercises=exercises)


@admin_bp.route("/add", methods=["POST"])
@login_required
def add():

    if not is_admin():
        return "No autorizado"

    ex = Exercise(
        english=request.form["english"],
        spanish=request.form["spanish"]
    )

    db.session.add(ex)
    db.session.commit()

    return redirect("/admin")