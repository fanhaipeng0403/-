# Register your models here.

# 主要作用是，是将Model注册到Django自带的admin里
from django.contrib import admin

from .models import Person

admin.site.register(Person)
