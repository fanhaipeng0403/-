"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from learn.views import index, add, add2

# Django2.0的 path 和 flask 很像
# https://kinegratii.github.io/2017/09/25/django2-url-path/
urlpatterns = [
    path('add/<int:a>/<int:b>/', add, name='add'),
    path('add2/', add2, name='add2'),
    path('', index),  # new
    path('admin/', admin.site.urls),
]
