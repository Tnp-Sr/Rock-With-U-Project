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
    path('admin', admin.site.urls),
    path('',include('homepage.urls')),
    path('index/',include('homepage.urls')),
    path('menu_P1/',include('homepage.urls')),
    path('menu_P2/',include('homepage.urls')),
    path('menu_P3/',include('homepage.urls')),
    path('menu_P4/',include('homepage.urls')),
    path('menu_P5/',include('homepage.urls')),
    path('menu_P6/',include('homepage.urls')),
    path('menu_P7/',include('homepage.urls')),
    path('menu_P8/',include('homepage.urls')),
    path('menuSearch/',include('homepage.urls')),
    path('registerForm/',include('homepage.urls')),
    path('addUser',include('homepage.urls')),
    path('loginForm/',include('homepage.urls')),
    path('login',include('homepage.urls')),
    path('logout/',include('homepage.urls')),
    path('orderHistory/',include('homepage.urls')),
    path('orderInfo/',include('homepage.urls')),
    path('cartDetails/',include('homepage.urls')),
    path('thanks/',include('homepage.urls')),
    path('test/',include('homepage.urls')),

]
