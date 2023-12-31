# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


class UserHandler(CommonHandler):
    # 预处理，url加载前
    def prepare(self):
        if not self.name:
            self.redirect("/login/")
