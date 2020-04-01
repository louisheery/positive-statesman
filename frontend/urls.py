from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^categories/(?P<path>.*)$', views.category),
    path('', views.index),
]
