"""djangomp URL Configuration

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

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<Post_id>[0-9]+)/$', views.specific, name='detail'),

    url(r'register', views.register, name = 'register'),

    url(r'home', views.Home, name = 'home'),

    url(r'logout', views.Logout, name = 'logout'),

    url(r'Cblog', views.Cblog, name = 'CBlog'),

    url(r'^(?P<Post_id>[0-9]+)/Update/', views.Update, name = 'Update'),

    url(r'^(?P<Post_id>[0-9]+)/Delete/', views.Delete, name = 'Delete'),

    url(r'^(?P<Post_id>[0-9]+)/tYp0zPar@sAuPd@t3/', views.up, name = 'tYp0zPar@sAuPd@t3'),

    url(r'^(?P<Post_id>[0-9]+)/0m9D3l3t3m3p0z1w@ntt01y@kn@p0z/', views.delet, name = '0m9D3l3t3m3p0z1w@ntt01y@kn@p0z'),
]
