# Register your models here.


# 这个模块的主要作用是，是将Model注册到Django自带的admin里
# 在flask一般使用flask_admin
# https://code.ziqiangxuetang.com/django/django-admin.html

from django.contrib import admin

from .models import Person

admin.site.register(Person)
