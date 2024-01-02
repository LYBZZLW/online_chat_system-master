from app.models.models import metadata
from app.configs import mysql_configs,channel_list
from sqlalchemy import create_engine
import mysql.connector  # 导入数据库连接驱动

if __name__ == "__main__":
    """ 用于初始化数据库 """
    # 创建连接引擎，连接地址、编码、是否输出日志
    # 连接格式：'数据库系统名称+连接驱动名称://用户:密码@主机:端口/数据库名称'
    engine = create_engine(
        'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8'.format(
            **mysql_configs
        ),
        echo=True
    )

    # 元类映射到数据库中去
    metadata.create_all(engine)
    # 给频道添加数据
    from app.models.crud import CRUD
    CRUD.channel_init(channel_list)