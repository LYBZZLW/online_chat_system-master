# -*- coding: utf-8 -*-
import tornado.web  # web框架
import tornado.ioloop  # 输入输出事件循环
import tornado.httpserver  # http服务
import tornado.options  # 选项配置，命令行解析

from tornado.options import define, options  # 定义，选项
from app.urls import urls  # 导入路由视图映射
from app.configs import configs, web_port  # 导入配置信息

# 定义服务启动的端口
define("port", type=int, default=web_port)


# 自定义应用
class CustomApplication(tornado.web.Application):
    # 定义初始化构造方法
    def __init__(self):
        handlers = urls  # 路由映射
        settings = configs  # 配置
        # 调用父类初始化方法，进行重载
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


# 定义创建http服务方法
def create_server():
    # 运行在命令行中启动
    tornado.options.parse_command_line()
    # 定义http server对象，传入自定义配置
    http_server = tornado.httpserver.HTTPServer(CustomApplication())
    # http server绑定端口，进行监控，服务进程启动
    http_server.listen(options.port)
    # 快速访问
    print('快速访问：http://localhost:{}'.format(web_port))
    # 启动输入输出事件循环
    tornado.ioloop.IOLoop.instance().start()
