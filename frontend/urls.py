from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^categories/(?P<path>.*)$', views.category),
    path('search/', views.index),
    path('', views.index),
]
