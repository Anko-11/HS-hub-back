from . import db
from werkzeug.security import generate_password_hash
import datetime


# class UserInfo(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(256), autoincrement=True)
#     name = db.Column(db.String(256), default=username)
#     password = db.Column(db.String(256))
#     user_level = db.Column(db.String(128), default=1)


#API授权表的模型
#多对多的关系
app_permission = db.Table("app_permission",
                          db.Column("api_id",db.ForeignKey("api_token.id")),
                          db.Column("permission_id",db.ForeignKey("api_permission.id"))
                          )
# api_token表
#存放的是授权密钥，以及授权id
class ApiToken(db.Model):
    __tablename__ = "api_token"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appid = db.Column(db.String(128), nullable=False)
    secretkey = db.Column(db.String(128), nullable=False)
    #通过中间表去创建多对多的关系
    manage = db.relationship("ApiPermission", secondary=app_permission, backref="token")

#存放的是授权的url
class ApiPermission(db.Model):
    __tablename__ = "api_permission"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128), nullable=False)
    method_type = db.Column(db.String(128), nullable=False)

class User(db.Model):
    __tablename__ = "userdb"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable = False)
    _password = db.Column("password", db.String(128), nullable=False)
    role = db.Column(db.Integer, default=0)
    add_time = db.Column(db.DateTime, default = datetime.datetime.now)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @classmethod
    def create_user(cls, username, password):
        user = cls()
        user.username = username
        user.password = password
        db.session.add(user)
        db.session.commit()
