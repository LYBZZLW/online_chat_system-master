# -*- coding: utf-8 -*-
from app.views.views_user import UserHandler
from app.tools.forms import UserEditForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD


class UserProfileHandler(UserHandler):
    def get(self, *args, **kwargs):
        if self.user:
            data = dict(
                title="个人资料",
                user=self.user
            )
            self.render("userprofile.html", data=data)

    def post(self, *args, **kwargs):
        res = dict(code=0)
        # 是否为注销请求
        if self.params.get('delete')[0] == 'yes':
            if CRUD.del_user(self.params.get('id')[0]):
                res['code'] = 1
            else:
                res['code'] = 0
        else:
            form = UserEditForm(MultiDict(self.params))
            if form.validate():
                if CRUD.save_user(form):
                    res['code'] = 1
            else:
                res = form.errors
                res["code"] = 0
        self.write(res)
