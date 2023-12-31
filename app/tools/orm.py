# -*- coding: utf-8 -*-
from sqlalchemy import create_engine  # 导入创建引擎工具
from sqlalchemy.orm import sessionmaker  # 会话创建工具
from app.configs import mysql_configs  # mysql配置


# 专门用于创建会话类
class ORM:
    @staticmethod
    def db():
        # 创建连接引擎
        engine = create_engine(
            "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8".format(
                **mysql_configs
            ),
            echo=False,
            pool_size=100,
            pool_recycle=10,
            connect_args={'charset': 'utf8'}
        )
        # 创建会话
        Session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )
        return Session()
