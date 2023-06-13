import imp
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='home'),
    path('nimcetscore',views.getNimcetScore, name='nimcet score'),
   
]