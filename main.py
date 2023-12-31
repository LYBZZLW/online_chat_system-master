from app import create_server

# 在第一次运行服务之前请在app/configs.py中进行配置，并运行app/models/models.py中的main函数用于初始化数据库
# 运行服务
if __name__ == '__main__':
    create_server()
