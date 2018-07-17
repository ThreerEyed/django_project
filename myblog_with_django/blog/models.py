from django.db import models


# blog 目录
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



