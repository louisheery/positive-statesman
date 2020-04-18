from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^categories/(?P<path>.*)$', views.index),
    path('search/', views.index),
    path('analytics/', views.index),
    path('', views.index),
]
