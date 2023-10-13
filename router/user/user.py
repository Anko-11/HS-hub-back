from . import user_db
from flask_restful import Resource, Api
from models.user import User
from libs.response import generate_response
from flask import request
from forms.user import UserForm, LoginForm
from libs.auth import create_token
from libs.handler import default_error_handler

api = Api(user_db)
api.handle_error = default_error_handler


class UserRegister(Resource):
    def post(self):
        # try:
        data = request.json
        form = UserForm(data=data)
        if form.validate():
            User.create_user(
                username=data.get("username"),
                password=form.password.data)
            return generate_response(message="注册成功", code=0)
        else:
            return generate_response(code=1, message=form.errors)

    # except:
    # return generate_response(code=1, message="注册失败!")
    # def post(self):
    #     username = request.json.get("username")
    #     password = request.json.get("password")
    #     role = request.json.get("role")
    #     User.creat_user(username, password)
    #     return generate_response(message="register success", code=1)


class LoginView(Resource):
    def post(self):
        data = request.json
        form = LoginForm(data=data)
        user = form.validate()
        if user:
            token = create_token(user.id)
            return generate_response(message="login success", code=0, data={"token": token,"username": user.username})
        else:
            return generate_response(message="login fail", code=1)


api.add_resource(UserRegister, "/user")
api.add_resource(LoginView, "/login")
