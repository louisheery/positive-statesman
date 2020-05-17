from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Count, Avg
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
from datetime import datetime, timedelta, timezone
import numpy as np
import pytz


def valid_filter(param):
    return param != '' and param is not None

def sortByRecommended(user, articles):
    # user_favourite_publishers = user.reader.popular_publisher.all()
    user_favourite_categories = user.reader.categories.all()
    user_favourite_category_names = [category.name for category in user_favourite_categories]
    scored_articles = []
    # algorithm, one point for publisher, one point for category, score * 10 points for sentiment
    for article in articles:
        article_categories = article.categories.all()
        articles_category_names = [category.name for category in article_categories]
        # pub_score = len(set([article.publisher]) & set(user_favourite_publishers))
        time_score = -((datetime.now(timezone.utc) - article.publish_date).days ** 2)
        cat_score = len(set(articles_category_names) & set(user_favourite_category_names))
        sent_score = article.sentiment_score * 2
        sort_score = cat_score + sent_score + time_score
        scored_articles.append({"score": sort_score,"article": article})
        print("score ", sort_score)

    scored_articles = sorted(scored_articles, key=lambda x: x['score'])
    scored_articles.reverse()
    print("first: ", scored_articles[0]["score"])
    print("last: ", scored_articles[len(scored_articles)-1]["score"])
    for x in scored_articles:
        print(x["score"])
    articles = [x["article"] for x in scored_articles]
    return articles

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

        # Only articles from last 24 hours
        # articles = articles.filter(publish_date__gte=(datetime.now() - timedelta(days=1)))

        # Order articles by publish date descending order
        articles = articles.order_by('-publish_date')

        # Only 1 Article of particular ID
        if valid_filter(id_only):
            articles = articles.filter(id=id_only)

        # Filter by Category, Publisher, Sentiment Score Range
        if valid_filter(category):
            if not category=="recommended":
                articles = articles.filter(categories__taxonomy_id=category)

        if valid_filter(publisher):
            articles = articles.filter(publisher__name=publisher)

        if valid_filter(sentiment_score_min):
            articles = articles.filter(
                sentiment_score__gte=sentiment_score_min)

        if valid_filter(sentiment_score_max):
            articles = articles.filter(sentiment_score__lt=sentiment_score_max)

        # Article Limit and Offset
        if valid_filter(category):
            if category=="recommended" and request.user.is_authenticated:
                user = request.user
                articles = sortByRecommended(user, articles)

        if valid_filter(articleOffset) and valid_filter(articleLimit):
            return articles[int(articleOffset): int(articleOffset) + int(articleLimit)]

        elif valid_filter(articleLimit):
            return articles[0: int(articleLimit)]

        else:
            return articles

            # articles = serializers.serialize('json', articles)
            # serializer = ArticleSerializer(articles, many=True)
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
    '''
    Let user create account
    '''
    _json = json.loads(request.body)
    if request.method == 'POST':
        user = User.objects.create_user(
            _json["username"], _json["email"], _json["password"])
        user.save()
        reader = Reader(user=user)
        reader.save()
        user = auth.authenticate(request, username=_json["username"], password=_json["password"])
        auth.login(request, user)
        return JsonResponse({"success": "success"}, status=200)


@csrf_exempt
def login(request):
    '''
    Let user login to account
    '''
    _json = json.loads(request.body)
    if request.method == 'POST':
        user = auth.authenticate(
            request, username=_json["username"], password=_json["password"])
        if user is not None:
            auth.login(request, user)
            return JsonResponse({"success": "success"}, status=200)
        else:
            return JsonResponse({"msg": "invalid user credentials"}, status=404)


@csrf_exempt
def logout(request):
    '''
    Let user logout of account
    '''
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({"err": "not logged in"}, status=200)
        auth.logout(request)
        return JsonResponse({"success": "success"}, status=200)


def popular_category(request):
    '''
    Get, add and delete category preferences for authenticated users
    '''
    if not request.user.is_authenticated:
        return JsonResponse({"msg": "User is not logged in"}, status=500)
    if request.method == 'DELETE':
        _json = json.loads(request.body)
        category = Category.objects.filter(taxonomy_id=_json["id"]).get()
        request.user.reader.categories.remove(category.id)
        return JsonResponse({"success": "success"}, status=200)
    elif request.method == 'GET':
        categories = request.user.reader.categories.all()
        information = [{"name": category.name, "id": category.id,
                        "tax_id": category.taxonomy_id} for category in categories]
        return JsonResponse({"info": information}, status=200)
    elif request.method == 'POST':
        _json = json.loads(request.body)
        category = Category.objects.filter(taxonomy_id=_json["id"]).get()
        reader = request.user
        reader = reader.reader
        reader.categories.add(category.id)
        return JsonResponse({"success": "success"}, status=200)
    else:
        return JsonResponse({"info": "no method found"}, status=404)


def popular_publisher(request):
    '''
    Get, add and delete publisher preferences for authenticated users
    '''
    if not request.user.is_authenticated:
        return JsonResponse({"msg": "User is not logged in"}, status=500)
    if request.method == 'DELETE':
        _json = json.loads(request.body)
        name = _json["name"].replace("%20", " ")
        publisher = Publisher.objects.filter(name=name).get()
        request.user.reader.publishers.remove(publisher)
        return JsonResponse({"success": "success"}, status=200)
    elif request.method == 'GET':
        publishers = request.user.reader.publishers.all()
        information = [{"name": publisher.name,"id": publisher.id} for publisher in publishers]
        return JsonResponse({"info":information}, status=200)
    elif request.method == 'POST':
        _json = json.loads(request.body)
        name = _json["name"].replace("%20", " ")
        publisher = Publisher.objects.filter(name=name).get()
        print(publisher)
        request.user.reader.publishers.add(publisher)
        return JsonResponse({"success": "success"}, status=200)


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

            articles = articles.filter(title__icontains=search_string) | articles.filter(
                text_snippet__icontains=search_string) | articles.filter(
                publisher__name__icontains=search_string) | articles.filter(
                categories__name__icontains=search_string)

        serializer = ArticleSerializer(articles.distinct(), many=True)

        if not articles:
            return HttpResponse(status=200)
        else:
            return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({"msg": "Only GET requests allowed."}, status=404)


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
            cat = ['iab-qagIAB3', 'iab-qagIAB11', 'iab-qagIAB17',
                   'iab-qagIAB1', 'iab-qagIAB15', 'iab-qagIAB19', 'iab-qagIAB20']
            count_list = []

            while cur_date <= end_date:

                timed_articles = articles.filter(
                    publish_date__gte=cur_date, publish_date__lte=cur_date+timedelta(days=1))

                for i in range(0, 7):
                    cat_articles = timed_articles.filter(
                        categories__taxonomy_id=cat[i])
                    if not cat_articles:
                        score_matrix[i] = 0
                    else:
                        score_matrix[i] = cat_articles.aggregate(Avg('sentiment_score'))[
                            'sentiment_score__avg']

                count_dict = {"date": cur_date.strftime("%Y-%m-%d"),
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

        elif param == 'locations':
            score_matrix = np.zeros(7)
            cur_date = begin_date
            cat = ['North America', 'South America', 'Africa',
                   'Europe', 'Asia', 'Oceania', 'Antarctica']
            count_list = []

            while cur_date <= end_date:

                timed_articles = articles.filter(
                    publish_date__gte=cur_date, publish_date__lte=cur_date+timedelta(days=1))

                for i in range(0, 7):
                    cat_articles = timed_articles.filter(
                        locations__name=cat[i])

                    if not cat_articles:
                        score_matrix[i] = 0
                    else:
                        score_matrix[i] = cat_articles.aggregate(Avg('sentiment_score'))[
                            'sentiment_score__avg']

                count_dict = {"date": cur_date.strftime("%Y-%m-%d"),
                              "north america": score_matrix[0],
                              "south america": score_matrix[1],
                              "europe": score_matrix[2],
                              "asia": score_matrix[3],
                              "africa": score_matrix[4],
                              "oceania": score_matrix[5],
                              "antarctica": score_matrix[6]
                              }

                count_list.append(count_dict)

                cur_date += timedelta(days=1)

            return JsonResponse(count_list, status=200, safe=False)

        elif param == 'countries':

            cur_date = begin_date
            cat = [
                "Afghanistan",
                "Angola",
                "Albania",
                "United Arab Emirates",
                "Argentina",
                "Armenia",
                "Antarctica",
                "Fr. S. Antarctic Lands",
                "Australia",
                "Austria",
                "Azerbaijan",
                "Burundi",
                "Belgium",
                "Benin",
                "Burkina Faso",
                "Bangladesh",
                "Bulgaria",
                "Bahamas",
                "Bosnia and Herz.",
                "Belarus",
                "Belize",
                "Bolivia",
                "Brazil",
                "Brunei",
                "Bhutan",
                "Botswana",
                "Central African Rep.",
                "Canada",
                "Switzerland",
                "Chile",
                "China",
                "Côte d'Ivoire",
                "Cameroon",
                "Dem. Rep. Congo",
                "Congo",
                "Colombia",
                "Costa Rica",
                "Cuba",
                "N. Cyprus",
                "Cyprus",
                "Czechia",
                "Germany",
                "Djibouti",
                "Denmark",
                "Dominican Rep.",
                "Algeria",
                "Ecuador",
                "Egypt",
                "Eritrea",
                "Spain",
                "Estonia",
                "Ethiopia",
                "Finland",
                "Fiji",
                "Falkland Is.",
                "France",
                "Gabon",
                "United Kingdom",
                "Georgia",
                "Ghana",
                "Guinea",
                "Gambia",
                "Guinea-Bissau",
                "Eq. Guinea",
                "Greece",
                "Greenland",
                "Guatemala",
                "Guyana",
                "Honduras",
                "Croatia",
                "Haiti",
                "Hungary",
                "Indonesia",
                "India",
                "Ireland",
                "Iran",
                "Iraq",
                "Iceland",
                "Israel",
                "Italy",
                "Jamaica",
                "Jordan",
                "Japan",
                "Kazakhstan",
                "Kenya",
                "Kyrgyzstan",
                "Cambodia",
                "South Korea",
                "Kosovo",
                "Kuwait",
                "Laos",
                "Lebanon",
                "Liberia",
                "Libya",
                "Sri Lanka",
                "Lesotho",
                "Lithuania",
                "Luxembourg",
                "Latvia",
                "Morocco",
                "Moldova",
                "Madagascar",
                "Mexico",
                "Macedonia",
                "Mali",
                "Myanmar",
                "Montenegro",
                "Mongolia",
                "Mozambique",
                "Mauritania",
                "Malawi",
                "Malaysia",
                "Namibia",
                "New Caledonia",
                "Niger",
                "Nigeria",
                "Nicaragua",
                "Netherlands",
                "Norway",
                "Nepal",
                "New Zealand",
                "Oman",
                "Pakistan",
                "Panama",
                "Peru",
                "Philippines",
                "Papua New Guinea",
                "Poland",
                "Puerto Rico",
                "North Korea",
                "Portugal",
                "Paraguay",
                "Palestine",
                "Qatar",
                "Romania",
                "Russia",
                "Rwanda",
                "W. Sahara",
                "Saudi Arabia",
                "Sudan",
                "S. Sudan",
                "Senegal",
                "Solomon Is.",
                "Sierra Leone",
                "El Salvador",
                "Somaliland",
                "Somalia",
                "Serbia",
                "Suriname",
                "Slovakia",
                "Slovenia",
                "Sweden",
                "Swaziland",
                "Syria",
                "Chad",
                "Togo",
                "Thailand",
                "Tajikistan",
                "Turkmenistan",
                "Timor-Leste",
                "Trinidad and Tobago",
                "Tunisia",
                "Turkey",
                "Taiwan",
                "Tanzania",
                "Uganda",
                "Ukraine",
                "Uruguay",
                "United States",
                "Uzbekistan",
                "Venezuela",
                "Vietnam",
                "Vanuatu",
                "Yemen",
                "South Africa",
                "Zambia",
                "Zimbabwe"
            ]
            score_matrix = np.zeros(len(cat))
            count_list = []

            while cur_date <= end_date:

                timed_articles = articles.filter(
                    publish_date__gte=cur_date, publish_date__lte=cur_date+timedelta(days=1))

                for i in range(0, len(cat)):
                    cat_articles = timed_articles.filter(
                        locations__name=cat[i])

                    if not cat_articles:
                        score_matrix[i] = 0
                    else:
                        score_matrix[i] = cat_articles.aggregate(Avg('sentiment_score'))[
                            'sentiment_score__avg']

                count_dict = {"date": cur_date.strftime("%Y-%m-%d")}

                for i in range(0, len(cat)):
                    count_dict[cat[i]] = score_matrix[i]

                count_list.append(count_dict)

                cur_date += timedelta(days=1)

            return JsonResponse(count_list, status=200, safe=False)

        else:
            return JsonResponse({"msg": "Not yet implemented"}, status=405)

    else:
        return JsonResponse({"msg": "Only GET requests allowed."}, status=405)

@csrf_exempt
def score_api(request):
    if request.method == 'POST':
        _json = json.loads(request.body)
        if not "text" in _json:
            return JsonResponse({"msg": "'text' field is required"}, status=422)
        text = _json["text"]
        if not isinstance(text, str):
            return JsonResponse({"msg": "'text' field must be a string"}, status=422)
        if len(text) < 100:
            return JsonResponse({"msg": "'text' string must be at least 100 characters"}, status=422)

        anaylser = SentimentIntensityAnalyzer()
        score = article_fetch.sentiment_score(anaylser, text)
        return JsonResponse({"score": score}, status=200)