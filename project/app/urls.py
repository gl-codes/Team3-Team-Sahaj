
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="HOME"),
     path('post', views.POST,name="POST"),
      path('transport', views.TRANSPORT,name="TRANSPORT"),
     path('signup', views.signup,name="signup"),
     path('signupage', views.signupage,name="signupage"),
      path('', views.register,name="index"),
      path('insert',views.insert,name="insert"),
]
