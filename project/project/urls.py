"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
  path('',views.index),
  path('index/',views.index),
  path('menu_P1/',views.menu_P1),
  path('menu_P2/',views.menu_P2),
  path('menu_P3/',views.menu_P3),
  path('menu_P4/',views.menu_P4),
  path('menu_P5/',views.menu_P5),
  path('menu_P6/',views.menu_P6),
  path('menu_P7/',views.menu_P7),
  path('menu_P8/',views.menu_P8),
  path('menuSearch/',views.menuSearch),
  path('registerForm/',views.registerForm),
  path('addUser',views.addUser),
  path('loginForm/',views.loginForm),
  path('login',views.login),
  path('logout/',views.logout),
  path('orderHistory/',views.orderHistory),
  path('orderQueue/',views.orderQueue),
  path('queueDetail',views.queueDetail),
  path('orderInfo/',views.orderInfo),
  path('cartDetails/',views.cartDetails),
  path('thanks/',views.thanks),
  path('test/',views.loginForm)
  

]
