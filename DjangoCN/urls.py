"""DjangoCN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Home import views as home_views

from User import views as user_views
from Manage import views as manage_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.index),
    url(r'^user$', user_views.index),
    url(r'^manage$', manage_views.index),


    url(r'^register$',home_views.register),
    url(r'^login$',home_views.login),
    url(r'^writeblogs$',user_views.writeblog),
    url(r'^viewblog$',user_views.viewblog),
]
