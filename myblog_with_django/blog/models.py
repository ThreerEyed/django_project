from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# blog 目录
from django.urls import reverse


class Category(models.Model):
    """
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    和目录一样定义标签的类
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """
    添加博客的字段
    1. 标题
    2. 创建时间，最后更新的时间
    3. 文章正文
    4. 总共阅读数量
    5. 文章摘要
    6. 各种关联字段
    """
    # 标题
    title = models.CharField(max_length=100)
    # 创建时间
    create_time = models.DateTimeField(default=datetime.now())
    # modified 修改时间
    modified = models.DateTimeField(default=datetime.now())
    # 文章正文
    content = models.TextField()
    # 总共阅读数量
    count = models.PositiveIntegerField(default=0)
    # 文章摘要或者文章在前
    excerpt = models.CharField(max_length=300, blank=True)

    # 外键关联字段, 目录和文章的关系是一对多的关系，所以这里我们采取一对多关联模式
    category = models.ForeignKey(Category)
    # 一个标签对应多个文章，一个文章也可以有多个标签，所以这里采用多对多的模式
    tag = models.ManyToManyField(Tag, blank=True)

    # 作者关联，这里我们采用的也是一对多的关联模式，一篇文章的作者通常只有一个，一个作者却可以有多篇文章
    # 这里的user 我们使用的是django 自带的user， 里面有这么几个字段
    # Username, password and email are required. Other fields are optional.
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('')





