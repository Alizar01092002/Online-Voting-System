from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('logout',views.logout,name="logout"),
    path('index',views.index,name="index"),
    path('vote',views.vote,name="vote")
]