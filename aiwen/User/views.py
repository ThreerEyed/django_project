import re

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from User.models import User
from utils import statucode
from utils.functions import get_ticket


def index(request):
    """首页视图"""
    if request.method == 'GET':
        return render(request, 'index/index.html')


def register(request):
    """注册视图, 这里会有问题，前端框架已有的验证，后端考虑是否不再验证，或者前端验证是否再重新处理一下"""
    if request.method == 'GET':
        # GET 请求就直接渲染页面
        return render(request, 'user/register.html')

    if request.method == 'POST':
        # post请求拿到表单数据
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('passwordAgain')
        captcha = request.POST.get('captcha')

        # 验证数据完整性
        if not all([phone, username, password, password_again, captcha]):
            return JsonResponse(statucode.DATA_NOT_COMPLETE)

        # 验证手机格式是否正确
        phone_reg = re.match('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', phone)
        if not phone_reg:
            return JsonResponse(statucode.PHONE_ERROR)

        # 验证用户名是否符合格式要求
        username_reg = re.match('^\w{6,20}', username)
        if not username_reg:
            return JsonResponse(statucode.USERNAME_FORMAT_ERROR)

        # 验证用户是否已存在
        user = User.objects.filter(Q(name=username) | Q(phone=phone)).first()
        if user:
            return JsonResponse(statucode.USER_EXISTS)

        # 验证密码是否符合要求
        password_reg = re.match('^\w{6,20}', password)
        if not password_reg:
            return JsonResponse(statucode.PASSWORD_FORMAT_ERROR)

        # 验证两次密码是否输入一致
        if password != password_again:
            return JsonResponse(statucode.PASSWORD_NOT_SAME)

        # 创建用户时候的默认头像
        avatar = 'user_avatar/default.png'
        # 创建用户的时候昵称就是注册时候的名字
        nickname = username
        user = User.objects.create(phone=phone, name=username, password=make_password(password),
                                   avatar=avatar, nickname=nickname)
        user.save()

        return JsonResponse({'code': statucode.OK})


def login(request):
    """登录视图"""
    if request.method == 'GET':
        return render(request, 'user/login.html')

    if request.method == 'POST':
        phone_or_name = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(Q(phone=phone_or_name) | Q(name=phone_or_name)).first()

        # 验证数据完整性
        if not all([phone_or_name, password]):
            return JsonResponse(statucode.DATA_NOT_COMPLETE)

        # 验证用户是否存在
        if not user:
            return JsonResponse(statucode.USER_NOT_EXISTS)

        # 验证密码是否正确
        if not check_password(password, user.password):
            return JsonResponse(statucode.USERNAME_OR_PASSWORD_ERROR)

        ticket = get_ticket()
        user = User.objects.filter(Q(phone=phone_or_name) | Q(name=phone_or_name)).first()
        user.ticket = ticket
        user.save()

        response = JsonResponse({'code': statucode.OK})
        response.set_cookie('ticket', ticket)
        return response


def login_status(request):
    """检查登录状态"""
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if User.objects.filter(ticket=ticket).first():
            user = User.objects.filter(ticket=ticket).first()
            avatar = user.avatar
            return JsonResponse({'code': statucode.OK, 'data': user.to_dict()})
        return JsonResponse(statucode.USER_NOT_LOGIN)


# 用户中心
def my(request):
    """用户中心"""
    if request.method == 'GET':
        return render(request, 'user/my.html')


# 用户设置
def setting(request):
    """用户设置"""
    if request.method == 'GET':
        return render(request, 'user/setting.html')


def set_avatar(request):
    """头像设置"""
    if request.method == 'GET':
        return render(request, 'user/setAvatar.html')

    if request.method == 'POST':
        image = request.FILES.get('file')

        ticket = request.COOKIES.get('ticket')
        user = User.objects.filter(ticket=ticket).first()
        if user:
            user.avatar = image
        user.save()

        src = '/median/' + image.name
        return JsonResponse({'code': statucode.OK, 'data': src})


def set_pwd(request):
    """密码修改"""
    print('====================')
    if request.method == 'GET':
        return render(request, 'user/set_pwd.html')

    if request.method == 'POST':
        print('=======')
        new_pwd = request.POST.get('password')
        new_pwd_confirm = request.POST.get('newpassword')

        user = User.objects.filter(ticket=request.COOKIES.get('ticket')).first()
        old_pwd = user.password

        # 验证数据完整性
        if not all([new_pwd, new_pwd_confirm]):
            return JsonResponse(statucode.DATA_NOT_COMPLETE)

        # 新旧密码不能相同
        if check_password(new_pwd, old_pwd):
            return JsonResponse(statucode.THE_SAME_PASSWORD)

        # 验证密码是否输入一致
        if new_pwd != new_pwd_confirm:
            return JsonResponse(statucode.PASSWORD_NOT_SAME)

        user.password = make_password(new_pwd_confirm)
        user.save()

        return JsonResponse({'code': statucode.OK})


def set_bind(request):
    """绑定邮箱"""
    if request.method == 'GET':
        return render(request, 'user/set_bind.html')
