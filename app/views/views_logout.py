# -*- coding: utf-8 -*-
from app.views.views_user import UserHandler


class LogoutHandler(UserHandler):
    def get(self, *args, **kwargs):
        # 清除cookie
        self.clear_cookie("name")
        self.redirect("/login/")
