from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),

    url(r'login_status/', views.login_status, name='login_status')
]

