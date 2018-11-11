# Create your models here.
from django.db import models


# 建议替换为sqlalchemy，下面的文章是对比
# http://www.zlovezl.cn/articles/sqlalchemy-intro-for-django-guys/

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

# 自定义字段类型
# https://code.ziqiangxuetang.com/django/django-custom-field.html
