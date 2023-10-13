from flask_sqlalchemy import SQLAlchemy

# 生成对象关系映射
db = SQLAlchemy()


# 绑定app
def init_app_db(app):
    db.init_app(app)


