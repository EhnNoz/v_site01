from django.contrib import admin
from django.urls import path
from myapp01 import views

urlpatterns=[
    path('salam', views.hello),
]