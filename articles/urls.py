from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
    path('user-feedback/', views.user_feedback),
    path('submit-article/', views.submit_article),
    path('search-articles/', views.search_articles),
    path('analytics/', views.article_average),
]

'''
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
]
'''
