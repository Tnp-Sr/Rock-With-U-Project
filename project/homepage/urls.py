from django.urls import path
from . import views

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