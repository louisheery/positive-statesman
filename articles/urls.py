from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
]

'''
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
]
'''
