from django.db import models

from User.models import User


class Article(models.Model):
    """文章类 用来管理文章"""

    a_id = models.AutoField(primary_key=True)                                             # 文章主键
    create_time = models.DateTimeField(auto_now_add=True)                                 # 创建时间
    update_time = models.DateTimeField(auto_now=True)                                       # 更新时间
    user = models.ForeignKey(User)                                                      # 关联到User表
    name = models.CharField(max_length=100, null=False)                                 # 文章标题
    abstract = models.CharField(max_length=100, null=True, blank=True)                  # 文章摘要
    category = models.CharField(max_length=50, null=True, blank=True)                   # 文章主目录
    second_category = models.CharField(max_length=50, null=True, blank=True)            # 文章次目录
    content = models.TextField()                                                         # 文章内容
    image = models.ImageField(upload_to='post')                                         # 文章图片
    tag = models.CharField(max_length=100)                                               # 文章标签
    source = models.CharField(max_length=50)                                             # 文章来源

    class Meta:
        db_table = 'article_tb'


class Collection(models.Model):
    """
    收藏

    """




