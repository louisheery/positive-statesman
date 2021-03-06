from django.urls import path
from articles import views
from django.contrib import admin


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.article_detail),
    path('fetch-articles/', views.fetch_articles),
    path('user-feedback/', views.user_feedback),
    path('submit-article/', views.submit_article),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('popular/category/', views.popular_category),
    path('popular/publisher/', views.popular_publisher),
    path('search-articles/', views.search_articles),
    path('analytics/', views.article_average),
    path('public/score/', views.score_api),
]
