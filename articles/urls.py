from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
    path('user-feedback/<int:article_pk>/', views.user_feedback),
    path('submit-article/', views.submit_article),
]

'''
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
]
'''
