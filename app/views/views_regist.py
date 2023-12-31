# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.forms import RegistForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD


class RegistHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="注册"
        )
        self.render("regist.html", data=data)

    # 通过post提交
    def post(self, *args, **kwargs):
        # 验证客户端提交参数
        form = RegistForm(MultiDict(self.params))
        res = dict(code=0)
        if form.validate():
            # 验证通过
            if CRUD.save_regist_user(form):
                res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        # 放回json格式数据
        self.write(res)
