from wtforms import Form, StringField
from wtforms.validators import DataRequired, Regexp, ValidationError
from models.user import User
from werkzeug.security import check_password_hash


class UserForm(Form):
    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired(), Regexp(r'\w{6,18}', message="密码不符合要求")])

    # 自定义验证器，验证邮箱是否唯一
    # 自定义检查字段 方法名：validate_你要检查的字段
    def validate_username(self, value):
        if User.query.filter_by(username = value.data).first():
            raise ValidationError("用户已存在")


class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired(), Regexp(r'\w{6,18}', message="密码不符合要求")])

    def validate(self):
        super().validate()
        if self.errors:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user and check_password_hash(user.password, self.password.data):
            return user
        else:
            raise ValidationError("验证失败！")

