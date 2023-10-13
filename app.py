import os
from flask import Flask
from libs.conn_mysql import conn_mysql


def creat_app():
    app = Flask(__name__)
    app.mysql_db = conn_mysql()
    app.config.from_object("config.settings")

    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    import router
    router.init_app(app)
    import models
    models.init_app_db(app)
    return app
