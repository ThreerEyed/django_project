from datetime import datetime

from django.db import models


class BaseMode(object):
    """定义基础模型 用于继承"""
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())


class User(BaseMode, models.Model):
    """
    定义 用户模型 用来存储用户的相关信息
    """
    # 用户名
    name = models.CharField(max_length=30, unique=True, null=False)
    # 用户手机号
    phone = models.CharField(max_length=11, unique=True, null=False)
    # 用户密码
    password = models.CharField(max_length=255, null=False)
    # ticket 用来存放用户的ticket
    ticket = models.CharField(max_length=100, null=True, blank=True)
    # 用户邮箱
    email = models.CharField(max_length=255, null=True, blank=True)
    # 昵称
    nickname = models.CharField(max_length=30, null=True, blank=True)
    # 个人头像
    avatar = models.ImageField(max_length=300, null=True, blank=True, upload_to='user_avatar')
    # 个人签名
    self_introduction = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'user_tb'

    def to_dict(self):
        return {
            'userId': self.id,
            'phone': self.phone,
            'username': self.name,
            'email': self.email,
            'nickname': self.nickname,
            'self_introduction': self.self_introduction

        }
