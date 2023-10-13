from .user import user_db


def init_app(app):
    app.register_blueprint(user_db)

