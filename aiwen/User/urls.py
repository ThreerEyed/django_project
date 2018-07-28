from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),

    url(r'login_status/', views.login_status, name='login_status'),
    # 用户中心
    url(r'my/', views.my, name='my'),
    # 用户设置
    url(r'setting/', views.setting, name='setting'),
    # 设置头像
    url(r'set_avatar/', views.set_avatar, name='set_avatar'),
    # 修改密码
    url(r'set_pwd/', views.set_pwd, name='set_pwd'),
    # 绑定邮箱
    url(r'set_bind/', views.set_bind, name='set_bind'),
    #
]

