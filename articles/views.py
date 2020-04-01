from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Q, Count, Avg
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from articles.models import Article, Category, Publisher
from articles.serializers import ArticleSerializer
from articles import article_fetch
from rest_framework import status
import json
from datetime import datetime, timedelta
import numpy as np
import pytz

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


def article_average(request):

    """ 
    Function to calculate the average sentiment score for an Article model parameter over a given timeframe
    
    Args:
        request: as the frontend request
        
    Returns:
        JsonResponse: The averaged scores
    """

    if request.method == 'GET':

        tz = pytz.timezone('Europe/London')

        begin_date = request.GET.get('begin')
        end_date = request.GET.get('end')
        param = request.GET.get('param')

        # 1. Date Checking
        try:
            begin_date = tz.localize(datetime.strptime(begin_date, '%Y-%m-%d'))
            end_date = tz.localize(datetime.strptime(end_date, '%Y-%m-%d'))
            print('Begin: ', begin_date)
        except:
            return JsonResponse({"msg": "Incorrect date representation."}, status=405)

        if end_date < begin_date:
            return JsonResponse({"msg": "Begin date is smaller than end date."}, status=405)

        # 2. Param Checking
        articles = Article.objects.all()

        if not valid_filter(param):
            return JsonResponse({"msg": "Incorrect param representation."}, status=405)
        
        # 3. Average calculation

        if param == 'categories':
            score_matrix = np.zeros(7)
            cur_date = begin_date
            cat = ['iab-qagIAB3', 'iab-qagIAB11', 'iab-qagIAB17', 'iab-qagIAB1', 'iab-qagIAB15', 'iab-qagIAB19', 'iab-qagIAB20']
            count_list = []

            while cur_date <= end_date:

                timed_articles = articles.filter(publish_date__gte=cur_date, publish_date__lte = cur_date+timedelta(days=1))
                
                for i in range(0,7):
                    cat_articles = timed_articles.filter(categories__taxonomy_id=cat[i])
                    if not cat_articles:
                        score_matrix[i] = 0
                    else:
                        score_matrix[i] = cat_articles.aggregate(Avg('sentiment_score'))['sentiment_score__avg']

                count_dict={"date": cur_date.strftime("%Y-%m-%d"),
                            "business": score_matrix[0],
                            "politics": score_matrix[1],
                            "sport": score_matrix[2],
                            "arts": score_matrix[3],
                            "science": score_matrix[4],
                            "technology": score_matrix[5],
                            "travel": score_matrix[6]
                }

                count_list.append(count_dict)

                cur_date += timedelta(days=1)

            return JsonResponse(count_list, status=200, safe=False)

        else:
            return JsonResponse({"msg": "Not yet implemented"}, status=405)


    else:
        return JsonResponse({"msg": "Only GET requests allowed."}, status=405)
