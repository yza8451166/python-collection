"""chouti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app01.views import account,home
from app01 import test



urlpatterns = [
    url(r'^admin', admin.site.urls),
    # url(r'^register/$', account.register),
    url(r'^check_code/$', account.check_code),
    url(r'^send_msg/$', account.send_msg),
    url(r'^register/$', account.register),
    url(r'^zan$',account.zan),
    url(r'^testcomment$',test.index),
    url(r'^comment$',test.comment),
    # url(r'^login/$', account.login),
    # url(r'^logout/$', account.logout),
    url(r'^', home.index),

]
