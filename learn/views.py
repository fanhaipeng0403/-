# coding:utf-8
from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎光临 自强学堂!")


def add2(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 定制url
def add(request, a, b):
    c = a + b
    return HttpResponse(str(c))
