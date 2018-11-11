# coding:utf-8
from django.http import HttpResponse

from learn.forms import AddForm


def index(request):
    return HttpResponse("欢迎光临 自强学堂!")




# 传统的
def add1(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 定制url
def add2(request, a, b):
    c = a + b
    return HttpResponse(str(c))



# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
def add3(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})