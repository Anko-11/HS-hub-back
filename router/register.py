# from flask import Blueprint
# from flask import request
# from libs.response import generate_response
# from models.user import UserInfo
# from models import db
#
# register_bp = Blueprint("register", __name__, url_prefix="/v1/")
#
#
# @register_bp.route("/register")
# def register():
#     username = request.json.get("username")
#     password = request.json.get("password")
#     if username == UserInfo.query.filter(UserInfo.username == username).first().username:
#         return generate_response(message="用户已存在", code=1)
#     else:
#         user = UserInfo()
#         user.username = username
#         user.password = password
#         db.session.add(user)
#         db.session.commit()
#         return generate_response(message="创建成功", code=0)
