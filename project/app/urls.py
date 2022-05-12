
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
     path('post', views.POST,name="POST"),
     path('MyPost', views.MyPost,name="MyPost"),
      path('transport', views.TRANSPORT,name="TRANSPORT"),
      path('', views.register,name="index"),
      path('insert',views.insert,name="insert"),
      path('signup',views.signupage,name="signup"),
      path('signuppage',views.handlesignup,name="handlesignup"),
      path('login',views.logn,name="login"),
      path('handlelogin',views.handlelogin,name="handlelogin"),
     
      path('logout',views.handlelogout,name="handlelogout"),
      path('Delete',views.delt,name="Delete"),
      path('display',views.display,name="display"),
]
