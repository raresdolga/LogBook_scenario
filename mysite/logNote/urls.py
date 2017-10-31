from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^home/', views.home, name='home'),
    url(r'^log-in/', views.welcomeLog, name='log-in'),
    url(r'^sign-in/', views.welcomeSign, name='sign-in')
]
