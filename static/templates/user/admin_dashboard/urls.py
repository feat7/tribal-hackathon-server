"""tribalhackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views import generic
from . import views


urlpatterns = [
    url(r'^allocations/all', views.allocations.all, name="allocations"),
    url(r'^schemes/all', views.schemes.all, name="schemes"),
    url(r'^announcements/all', views.announcements.all, name="announcements"),
    url(r'^scheme/(?P<id>(\d+))/like$', views.schemes.like),
    url(r'^scheme/(?P<id>(\d+))/dis_like$', views.schemes.dis_like),
    url(r'^places/all', views.places.all, name="places"),
    url(r'^departments/all', views.departments.all, name="departments"),
    url(r'^place-search/(?P<id>(\d+))$', views.places.search),
    url(r'^graph/(?P<used>(\d+))/(?P<allocated>(\d+))$', views.graphs.normal),
    url(r'^schemes', views.schemes.view_all),
]
