# -*- coding: utf-8 -*-
from wtforms import Form  # 导入父类
from wtforms.fields import StringField, PasswordField, IntegerField  # 导入字段类型
from wtforms.validators import DataRequired, Regexp, Email, EqualTo, ValidationError  # 导入验证器

from app.models.crud import CRUD


# 注册表单验证
class RegistForm(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired("昵称不能为空！")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired("密码不能为空！")
        ]
    )
    repwd = PasswordField(
        "确认密码",
        validators=[
            DataRequired("确认密码不能为空！"),
            EqualTo("pwd", message="两次输入密码不一致！")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空！"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确！")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if data:
            raise ValidationError("昵称已经存在了！")

    # 自定义验证邮箱
    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if data:
            raise ValidationError("邮箱已经存在了！")

    # 自定义验证手机
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if data:
            raise ValidationError("手机号码已经存在！")


# 登录表单验证
class LoginForm(Form):
    name = StringField(
        "账号",
        validators=[
            DataRequired("账号不能为空！")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired("密码不能为空！")
        ]
    )

    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("账号不存在！")

    def validate_pwd(self, field):
        if not CRUD.check_login(self.name.data, field.data):
            raise ValidationError("密码不正确！")


# 用户中心表单验证
class UserEditForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    name = StringField(
        "昵称",
        validators=[
            DataRequired("昵称不能为空！")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空！"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确！")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ]
    )
    face = StringField(
        "头像",
        validators=[]
    )
    info = StringField(
        "个性签名",
        validators=[]
    )
    sex = IntegerField(
        "性别",
        validators=[]
    )
    constellation = IntegerField(
        "星座",
        validators=[]
    )
