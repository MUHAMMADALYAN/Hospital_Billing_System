from django.contrib import admin
from django.urls import path
from module1 import views

urlpatterns = [
    path('', views.home),
    path('home.html', views.home),
    path('datas',views.datas),
    path('reports',views.reports),
    path('masters',views.masters),
    path('contact.html',views.contact)
]
