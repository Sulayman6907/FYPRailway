from login import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', views.loginPage),
    path('home/', views.home),
    path('run/', views.run),
    path('check/', views.check),
    path('change/', views.change),
    path('saveFile/', views.saveFile),
    path('getData/', views.getData),
]