from .views import check
from django.urls import path, include
from django.contrib import admin

urlpatterns = [path("check/", check, name="check")]
