from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from articles.models import Article, Category, Publisher, Reader
from articles.serializers import ArticleSerializer
from articles import article_fetch
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib import auth
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

@csrf_exempt
def signup(request):
    _json = json.loads(request.body)
    if request.method == 'GET':
        usernames = User.objects.values_list('username', flat=True)
        usernames = [username for username in usernames]
        return JsonResponse({"msg": usernames}, status=404)
    if request.method == 'POST':
        user = User.objects.create_user(_json["username"],_json["email"], _json["password"])
        user.save()
        reader = Reader(user=user)
        reader.save()
        user = auth.authenticate(request, username=_json["username"], password=_json["password"])
        return JsonResponse({"success": "success"}, status=200)

@csrf_exempt
def login(request):
    _json = json.loads(request.body)
    if request.method == 'POST':
        user = auth.authenticate(request, username=_json["username"], password=_json["password"])
        if user is not None:
            auth.login(request, user)
            return JsonResponse({"success": "success"}, status=200)
        else:
            return JsonResponse({"msg": "invalid user credentials"}, status=404)

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({"err": "not logged in"}, status=500)
        auth.logout(request)
        return JsonResponse({"success": "success"}, status=200)

def popular_category(request):
    _json = json.loads(request.body)
    if not request.user.is_authenticated:
        return JsonResponse({"msg": "User is not logged in"}, status=500)
    if request.method == 'POST':
        category = Category.objects.filter(taxonomy_id=_json["id"]).get()
        reader = request.user
        reader = reader.reader
        reader.categories.add(category.id)
        return JsonResponse({"success": "success"}, status=200)
    if request.method == 'DELETE':
        category = Category.objects.filter(taxonomy_id=_json["id"]).get()
        request.user.reader.categories.remove(category.id)
        return JsonResponse({"success": "success"}, status=200)
    if request.method == 'GET':
        categories = request.user.reader.categories.all()
        information = [{"name": category.name,"id": category.id,"tax_id": "id": category.taxonomy_id} for category in categories]
        return JsonResponse(information, 200)

def popular_publisher(request):
    _json = json.loads(request.body)
    if not request.user.is_authenticated:
        return JsonResponse({"msg": "User is not logged in"}, status=500)
    if request.method == 'POST':
        request.user.reader.popular_publisher.add(_json["id"])
        return JsonResponse({"success": "success"}, status=200)
    if request.method == 'DELETE':
        request.user.reader.popular_publisher.remove(_json["id"])
        return JsonResponse({"success": "success"}, status=200)
    if request.method == 'GET':
        publishers = request.user.reader.popular_publisher.all()
        information = [{"name": category.name,"id": category.id} for category in publishers]
        return JsonResponse(information, 200)
