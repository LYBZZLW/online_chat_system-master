# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSRouter
from app.views.views_chat import ChatHandler as chat
from app.views.views_regist import RegistHandler as regist
from app.views.views_login import LoginHandler as login
from app.views.views_userprofile import UserProfileHandler as userprofile
from app.views.views_logout import LogoutHandler as logout
from app.views.views_upload import UploadHandler as upload
from app.views.views_chatroom import ChatRoomHandler as chatroom
from app.views.views_msg import MSGHandler as msg
from app.views.views_channel import ChannelHandler as channel
# 路由视图映射：(路由地址,视图)
urls = [
           (r"/", chat),
           (r"/regist/", regist),
           (r"/login/", login),
           (r"/logout/", logout),
           (r"/upload/", upload),
           (r"/msg/", msg),
           (r"/userprofile/", userprofile),
           (r"/channel/", channel)
        ] + SockJSRouter(chatroom, "/chatroom").urls
