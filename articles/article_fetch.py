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
            categories_id=['IAB15-10', 'IAB11', 'IAB3', 'IAB17'],
            #source_domain=['bbc.co.uk', 'news.yahoo.com', 'yahoo.com', 'guardian.co.uk', ],
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

############################## FUNCTION TESTING ###############################

# TEST: fetch_metadata(...)

# TEST: get_full_text(...)

# TEST: sentiment_score(...)

sentiment_analyser = SentimentIntensityAnalyzer()
sample_text = "Hospitals in the Chinese city of Wuhan have been \
 thrown into chaos and the movement of about 33 million people has been \
    restricted by an unprecedented and indefinite lockdown imposed to halt the \
        spread of the deadly new coronavirus. At least 10 cities in central \
            Hubei province have been shut down in an effort to stop the virus, \
                which by Friday had killed 26 people across China and affected \
                    more than 800. The World Health Organisation described the \
                        outbreak as an emergency for China, but stopped short \
                            of declaring it to be a public health emergency of \
                                international concern."

print("Compound Sentiment Score: ", sentiment_score(sentiment_analyser, sample_text))

# TEST: generate_articles(...)

################################# DRIVER CODE #################################
"""
generate_articles()
"""
