"""
Description:    Article Scraping and Sentiment Analaysis Script for MVP
Author:         ms519, lhs19, mgeorge2
TODO:
- Set up requirements.txt:
    -> pip3 install vaderSentiment
    -> pip3 install newsapi-python 
- Write / finish functions:
   - generate_articles()
   - fetch_metadata()
   - get_full_text()
- Write function tests 
- Figure out what error message means:
    django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import aylien_news_api
from aylien_news_api.rest import ApiException
from articles.models import Article, Publisher, Location, Category
from articles.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse


############################# FUNCTION DEFINITION #############################

def generate_articles():
    
    """
    Function to generate article models to put into the database.
    Args:
        none
    Returns:
        none
    """

    apikey = "087e404043fb6f7df4c4ed55e72f3f7f"
    appid = "dc8dc66d"
    configuration = aylien_news_api.Configuration()
    configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = appid
    configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = apikey

    client = aylien_news_api.ApiClient(configuration)
    api_instance = aylien_news_api.DefaultApi(client)
    
    # 1.    Fetch articles

    api_response = fetch_articles(api_instance)
    stories = api_response.stories
    # TBD error handling

    # 2.    Get the full text for every article
    # 2.1       Analyse sentiment
    for story in stories:
        save_from_story(story)
        


def fetch_articles(api_instance):
    try:
        api_response = api_instance.list_stories(
            published_at_start='NOW-1DAYS',
            published_at_end='NOW',
            per_page=100,
            categories_taxonomy='iab-qag',
            categories_id=['IAB1', 'IAB3', 'IAB11', 'IAB15', 'IAB17', 'IAB19', 'IAB20'],
            #source_domain=['bbc.co.uk', 'news.yahoo.com', 'yahoo.com', 'guardian.co.uk', ],
            source_domain=["theguardian.com","nytimes.com","ft.com","bloomberg.com","reuters.com","apnews.com","thetimes.co.uk","washingtonpost.com","afp.com","abcnews.go.com","time.com","wsj.com","economist.com","politico.com",
            "bbc.com","pbs.com","thehill.com","usatoday.com","npr.org","cbsnews.com","axios.com","huffpost.com","newyorker.com","nationalreview.com","slate.com","theatlantic.com","theweek.com","vanityfair.com","msnbc.com","cnn.com",
            "theamericanconservative.com","vox.com","mic.com","independent.co.uk","thesun.co.uk","metro.co.uk","dailymail.co.uk","telegraph.co.uk","latimes.com","cnet.com","engadget.com","theverge.com","vice.com","hollywoodreporter.com",
            "newsweek.com","forbes.com","sciencemag.org","rte.com","natgeo.com","wanderlust.co.uk","skysports.com","espn.com","theathletic.co.uk","phys.org","physicsworld.com","sky.com","techradar.com","entertainmentdaily.co.uk",
            "digitalspy.com","inews.co.uk","ign.com","france24.com","dw.com","euronews.com","thelocal.it","elpais.com","cbc.ca","globalnews.ca","nationalpost.com","msn.com","nbcnews.com","abc.net.au","scmp.com","seattletimes.com",
            "independent.ie","standard.co.uk","wired.co.uk","fortune.com","techcrunch.com","usnews.com"],
            language=['en'],
            #next_page_cursor=next_page_cursor
        )
        return api_response
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)


def save_article(url):
    apikey = "087e404043fb6f7df4c4ed55e72f3f7f"
    appid = "dc8dc66d"
    configuration = aylien_news_api.Configuration()
    configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = appid
    configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = apikey
    client = aylien_news_api.ApiClient(configuration)
    api_instance = aylien_news_api.DefaultApi(client)
    try:
        print("URRRLLLL:")
        print(url)
        api_response = api_instance.list_stories(
            published_at_end='NOW',
            links_permalink=[url],
        )
        if len(api_response.stories) == 0:
            return JsonResponse({"msg": "No article found for this url"}, status=404)
        if len(api_response.stories) > 1:
            # print(api_response.stories)
            return JsonResponse({"msg": "More than one article found for this url. Articles found: " + str(len(api_response.stories))}, status=404)

        story = api_response.stories[0]
        save_from_story(story)
        return JsonResponse({"msg": "Success"}, status=200)

    except ApiException as e:
        return JsonResponse({"msg": "Internal API error"}, status=500)


def sentiment_score(analyser, text):

    """
    Analyse the sentiment score of a given string.
    Args:
        analyser(SentimentIntensityAnalyser): Vader analyser
        text(string): string of the article to be analysed
    Returns:
        scores['compound'](int): compound sentiment score of the article
    """

    scores = analyser.polarity_scores(text)
    return scores['compound']

def save_from_story(story):
    title = story.title
    publish_date = story.published_at
    url = story.links.permalink
    publisher = Publisher.objects.get_or_create(name=story.source.name)[0]
    image_url = ''
    for media in story.media:
        if (media.type == 'image'):
            image_url = media.url
    full_text = story.body
    vader_analyser = SentimentIntensityAnalyzer()
    s_score = sentiment_score(vader_analyser, full_text)

# 2.2       Create Article Model Instances

    ## Database integration not working yet ##            
    publisher, created = Publisher.objects.get_or_create(
        name=story.source.name,
    )
    publisher.url = story.source.home_page_url
    publisher.save()


    article, created = Article.objects.get_or_create(
        url=url,
        defaults={
        'title':title,
        'image_url':image_url,
        'publisher':publisher,
        'publish_date':publish_date,
        'sentiment_score':s_score,
        'text_full':full_text})


    for entity in story.entities.body:
        location_type = False
        if "City" in entity.types:
            location_type = "city"
        if "Region" in entity.types:
            location_type = "region"
        if "Country" in entity.types:
            location_type = "country"
        if location_type:
            location, created = Location.objects.get_or_create(
                name=entity.text,
                location_type=location_type
            )
            article.locations.add(location)

    for category in story.categories:
        tax_id = category.taxonomy + category.id
        category = Category.objects.filter(taxonomy_id=tax_id).first()
        article.categories.add(category)

    return
