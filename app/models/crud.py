# -*- coding: utf-8 -*-
import datetime

from app.tools.orm import ORM
from app.models.models import User, Msg, Channel
from werkzeug.security import generate_password_hash


def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 增删改查的类
class CRUD(object):
    # 验证用户唯一性，1昵称，2邮箱，3手机
    @staticmethod
    def user_unique(data, method=1):
        # 1.调用会话
        session = ORM.db()
        user = None
        # 2.查询逻辑，事务处理
        try:
            # 执行增删改查
            model = session.query(User)
            if method == 1:
                # 验证昵称
                user = model.filter_by(name=data).first()
            if method == 2:
                # 验证邮箱
                user = model.filter_by(email=data).first()
            if method == 3:
                # 验证手机
                user = model.filter_by(phone=data).first()
        except Exception as e:
            # 发生异常回滚
            session.rollback()
        else:
            # 没有发生异常提交
            session.commit()
        finally:
            # 无论是否发生异常，关闭会话
            session.close()

        if user:
            return True
        else:
            return False

    # 保存注册用户
    @staticmethod
    def save_regist_user(form):
        session = ORM.db()
        try:
            user = User(
                name=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data["email"],
                phone=form.data["phone"],
                sex=None,
                constellation=None,
                face="default.png",
                info=None,
                create_date=dt(),
                update_date=dt()
            )
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 检测登录
    @staticmethod
    def check_login(name, pwd):
        session = ORM.db()
        result = False
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                if user.check_pwd(pwd):
                    result = True
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 根据昵称查询用户
    @staticmethod
    def user(name):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(name=name).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user

    # 保存用户数据
    @staticmethod
    def save_user(form):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(id=int(form.data['id'])).first()
            user.name = form.data['name']
            user.email = form.data['email']
            user.phone = form.data['phone']
            user.sex = form.data.get('sex')
            user.constellation = form.data.get('constellation')
            user.face = form.data['face']
            user.info = form.data['info']
            user.update_date = dt()
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 保存消息
    @staticmethod
    def save_msg(content, name, channel):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                user_id = user.id
            else:
                user_id = 0
            msg = Msg(
                content=content,
                create_date=dt(),
                update_date=dt(),
                channel_id=channel,
                user_id=user_id
            )

            session.add(msg)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 加载消息
    @staticmethod
    def lastest_msg():
        session = ORM.db()
        data = []
        try:
            data = session.query(Msg).order_by(Msg.create_date.desc()).limit(300).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 注销用户
    @staticmethod
    def del_user(user_id):
        session = ORM.db()
        try:
            session.query(User).filter(User.id == user_id).delete()
            session.query(Msg).filter(Msg.user_id == user_id).delete()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 读取频道名
    @staticmethod
    def load_channel():
        session = ORM.db()
        data = []
        try:
            data = session.query(Channel).order_by(Channel.id.desc()).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 初始化频道
    @staticmethod
    def channel_init(name_list):
        session = ORM.db()
        try:
            session.query(Channel).delete()
            for name in name_list:
                channel = Channel(name=name)
                session.add(channel)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True