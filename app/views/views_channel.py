# -*- coding: utf-8 -*-
from app.models.crud import CRUD
from app.views.views_common import CommonHandler


class ChannelHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def get(self, *args, **kwargs):
        data = CRUD.load_channel()
        result = []
        for v in data:
            result.append((v.id, v.name))
        d=dict(data=result[::-1])
        self.write(d)
