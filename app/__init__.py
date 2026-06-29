import os
from flask import Flask
from app.extensions import db, login_manager, bcrypt

def create_app():

    base_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.join(base_dir, "..")

    app = Flask(
        __name__,
        template_folder=os.path.join(project_root, "templates")
    )

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = "auth.login"

    # 🔥 BLUEPRINTS (ESTO TE FALTABA)
    from app.auth import auth_bp
    from app.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app