from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth  # 认证 其中authenticate()函数给出用户名密码
from django.contrib.auth.decorators import login_required  # 关窗户 导入包


# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse(u"Hello Django!")


# 登录动作
# @login_required
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response =  HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600) # 添加浏览器的cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':u'用户名或密码错误！'})


# 发布会管理
@login_required   # 关窗户，避免不登录直接可访问登录页面，限制视图函数event_manage
def event_manage(request):
    # username = request.COOKIES.get('user','')  # 读取浏览器cookie
    username = request.session.get('user','')  # 读取浏览器session
    return render(request,"event_manage.html",{"user":username})