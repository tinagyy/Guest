"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import  views #导入sign应用的views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),  # 添加index/路径配置,访问 http://127.0.0.1:8000/index  跳转到首页index
    url(r'^login_action/$',views.login_action),
    # url(r'^login_action/$',views.index),
    url(r'^event_manage/$',views.event_manage),
    url(r'^accounts/login/$',views.index),  # 访问 http://127.0.0.1:8000/event_manage  跳转到首页index；event_manage前面加了限制，必须登录才能访问
    url(r'^$',views.index),    # 访问 http://127.0.0.1:8000/  跳转到首页index
]
