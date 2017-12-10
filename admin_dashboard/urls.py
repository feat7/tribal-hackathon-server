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
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
    url(r'^allocations/all', views.allocations.all, name="allocations"),
    url(r'^schemes/all', views.schemes.all, name="schemes"),
    url(r'^places/all', views.places.all, name="places"),
    url(r'^departments/all', views.departments.all, name="departments"),
    url(r'^place-search/(?P<id>(\d+))$', views.places.search),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^all', views.list_all_places),
    # url(r'^complaints/all', views.complaints.all),
    # url(r'^', views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from . import views
>>>>>>> 1b0ba044e93796d7d6828104798b7bc34c48f650
