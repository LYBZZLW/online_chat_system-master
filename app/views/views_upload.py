# -*- coding: utf-8 -*-
import os
import datetime
import uuid
from app.views.views_common import CommonHandler


# 上传头像
class UploadHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def post(self, *args, **kwargs):
        files = self.request.files["img"]
        imgs = []
        # 指定保存目录
        upload_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    __file__
                )
            ), "static/uploads"
        )
        # 判断目录是否存在，不存在创建
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)

        for v in files:
            # 文件格式：时间+唯一标志+后缀
            prefix1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            prefix2 = uuid.uuid4().hex
            newname = prefix1 + prefix2 + os.path.splitext(v['filename'])[-1]
            with open(os.path.join(upload_path, newname), "wb") as up:
                up.write(v['body'])
            imgs.append(newname)
        res = dict(
            code=1,
            image=imgs[0]
        )
        self.write(res)
