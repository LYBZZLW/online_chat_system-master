# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 创建模型继承的父类
from sqlalchemy.dialects.mysql import BIGINT, TEXT, DATETIME, VARCHAR, TINYINT  # 导入字段类型
from sqlalchemy import Column  # 定义字段
from werkzeug.security import check_password_hash  # 检查密码

# 创建父类
Base = declarative_base()
metadata = Base.metadata


# 创建消息保存模型
class Msg(Base):
    __tablename__ = "msg"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    content = Column(TEXT, comment='文本')  # 内容
    create_date = Column(DATETIME, nullable=False)  # 创建时间
    update_date = Column(DATETIME, nullable=False)  # 修改时间
    channel_id = Column(BIGINT, nullable=False, comment='频道编号')  # 频道编号
    user_id = Column(BIGINT, nullable=False, comment='用户编号')  # 用户的编号（1对多）


# 创建会员模型
class User(Base):
    __tablename__ = "user"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    name = Column(VARCHAR(20), nullable=False, unique=True)  # 昵称
    pwd = Column(VARCHAR(255), nullable=False)  # 密码
    email = Column(VARCHAR(100), nullable=False, unique=True)  # 邮箱
    phone = Column(VARCHAR(11), nullable=False, unique=True)  # 手机
    sex = Column(TINYINT, nullable=True)  # 性别
    constellation = Column(TINYINT, nullable=True, comment='星座')  # 星座
    face = Column(VARCHAR(100), nullable=True, comment='头像url')  # 头像
    info = Column(VARCHAR(600), nullable=True, comment='简述')  # 介绍
    create_date = Column(DATETIME, nullable=False)  # 创建时间
    update_date = Column(DATETIME, nullable=False)  # 修改时间

    # 验证密码
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 创建频道模型
class Channel(Base):
    __tablename__ = "channel"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    name = Column(VARCHAR(20), nullable=False, unique=True, comment='频道名')  # 频道名
