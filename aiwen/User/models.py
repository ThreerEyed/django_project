from datetime import datetime

from django.db import models


class Base(models.Model):
    """定义基础模型 用于继承"""
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())


class User(Base):
    """
    定义 用户模型 用来存储用户的相关信息
    """
    # 用户id
    user_id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    # 用户名
    name = models.CharField(max_length=30, unique=True, null=False)
    # 用户手机号
    phone = models.CharField(max_length=11, unique=True, null=False)
    # 用户密码
    password = models.CharField(max_length=255, null=False)
    # 用户邮箱
    email = models.CharField(max_length=255, null=True)
    # 昵称
    nickname = models.CharField(max_length=30, null=True)
    # 个人头像
    avatar = models.CharField(max_length=300, null=True)
    # 个人签名
    self_introduction = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'user_tb'


