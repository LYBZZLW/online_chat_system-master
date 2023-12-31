# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


# 聊天视图，RequestHandler封装请求和响应所有操作
class ChatHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="聊天室"
        )
        self.render("chat.html", data=data)
