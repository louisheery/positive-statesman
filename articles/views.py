from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q, Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from articles.models import Article, Category, Publisher
from articles.serializers import ArticleSerializer
from articles import article_fetch
from rest_framework import status
import json


def valid_filter(param):
    return param != '' and param is not None


def article_filter(request):
    '''
    List articles according to a particular filter
    '''

    if request.method == 'GET':

        articles = Article.objects.all()
        categories = Category.objects.all()
        publishers = Publisher.objects.all()

        category = request.GET.get('category')
        publisher = request.GET.get('publisher')
        id_only = request.GET.get('id')
        sentiment_score_min = request.GET.get('sentiment_score_min')
        sentiment_score_max = request.GET.get('sentiment_score_max')

        articleLimit = request.GET.get('limit')
        articleOffset = request.GET.get('offset')

        # Only 1 Article of particular ID
        if valid_filter(id_only):
            articles = articles.filter(id=id_only)

        # Filter by Category, Publisher, Sentiment Score Range
        if valid_filter(category):
            articles = articles.filter(categories__taxonomy_id=category)

        if valid_filter(publisher):
            articles = articles.filter(publisher__name=publisher)

        if valid_filter(sentiment_score_min):
            articles = articles.filter(
                sentiment_score__gte=sentiment_score_min)

        if valid_filter(sentiment_score_max):
            articles = articles.filter(sentiment_score__lt=sentiment_score_max)

        # Article Limit and Offset
        if valid_filter(articleOffset) and valid_filter(articleLimit):
            return articles[int(articleOffset): int(articleOffset) + int(articleLimit)]

        elif valid_filter(articleLimit):
            return articles[0: int(articleLimit)]

        else:
            return articles

            #articles = serializers.serialize('json', articles)
            #serializer = ArticleSerializer(articles, many=True)
            # print(serializer)
            # return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class ArticleList(generics.ListAPIView):

    serialiserClass = ArticleSerializer

    def get_queryset(self):
        articles = article_filter(self.request)
        return articles

    def list(self, request):
        articles = self.get_queryset()
        serialiser = self.serialiserClass(articles, many=True)
        return Response(serialiser.data)


def article_detail(request, pk):
    """
    Retrieve, update or delete an article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)


def fetch_articles(request):
    if request.method == 'GET':
        print("success")
        article_fetch.generate_articles()
        return JsonResponse({"response": "success"}, safe=False)


def user_feedback(request):
    _json = json.loads(request.body)
    try:
        article_pk = _json['pk']
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        return JsonResponse({"msg": "No article found with specified pk"}, status=404)

    if request.method == 'POST':
        vote = _json['vote']
        if vote == "positive" or vote == "neutral" or vote == "negative":
            if vote == "positive":
                article.user_score_positive += 1
            if vote == "neutral":
                article.user_score_neutral += 1
            if vote == "negative":
                article.user_score_negative += 1
            article.user_score_count += 1
            article.save()
            return JsonResponse({"msg": "Vote added to database"}, status=200)
        return JsonResponse({"msg": "Vote value in body invalid"}, status=404)


def submit_article(request):
    _json = json.loads(request.body)
    url = _json['url']
    print(url)

    return article_fetch.save_article(url)

def search_articles(request):
    
    """ 
    Function to return title and snippet search results of a given request 
    
    Args:
        request: as the frontend request
    
    Returns:
        JsonResponse: The matched articles
    """

    if request.method == 'GET':

        articles = Article.objects.all()
        search_string = request.GET.get('search')

        if search_string != '':

            articles = articles.filter(title__icontains = search_string) | articles.filter(text_snippet__icontains = search_string)

        serializer = ArticleSerializer(articles.distinct(), many=True)

        if not articles:
            return HttpResponse(status=200)
        else:
            return JsonResponse(serializer.data, safe=False)
        
    else:
        return JsonResponse({"msg": "Only GET requests allowed."}, status=404)


