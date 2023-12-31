# -*- coding: utf-8 -*-
import json

from app.views.views_common import CommonHandler
from app.models.crud import CRUD


class MSGHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def post(self, *args, **kwargs):
        data = CRUD.lastest_msg()
        result = []
        for v in data:
            result.append(json.loads(v.content))
        d=dict(data=result[::-1])
        self.write(d)
