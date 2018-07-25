from django.shortcuts import render


def index(request):
    """首页视图"""
    if request.method == 'GET':
        return render(request, 'index/index.html')


def register(request):
    """注册视图"""
    if request.method == 'GET':
        return render(request, 'user/register.html')


def login(request):
    """登录视图"""
    if request.method == 'GET':
        return render(request, 'user/login.html')



