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
from newsapi import NewsApiClient
import models

############################# FUNCTION DEFINITION #############################

def generate_articles():
    
    """
    Function to generate article models to put into the database.

    Args:
        none

    Returns:
        none

    """

    api_client = NewsApiClient(api_key = '9d8a507d17344549bada8196027fe870')
    vader_analyser = SentimentIntensityAnalyzer()
    
    # 1.    Fetch metadata

    meta_list = fetch_metadata(api_client)

    # 2.    Get the full text for every article

    for meta in meta_list:
        full_text = get_full_text(meta[0])

    # 2.1       Analyse sentiment

        s_score = sentiment_score(vader_analyser, full_text)
    
    # 2.2       Create Article Model Instances

        ## Database integration not working yet ##
        # p = models.Article.create(meta[0],meta[1],meta[2],meta[3],meta[4],meta[6],s_score)
        # p.save()

def fetch_metadata(api_client):

    """
    Function to fetch article metadata from news-api.

    Args:
        api_client(NewsApiClient): News API client object, provided from generate_articles()

    Returns:
        meta_list(list): List of fetched metadata

    """
    ## TO BE IMPLEMENTED ##

    meta_list = []
    return meta_list


def get_full_text(link):

    """
    Fetch full text of an article based on a link using alyien.

    Args:
        link(string): URL of the article to be fetched

    Returns:
        full_text(list): full article text

    """
    ## TO BE IMPLEMENTED ##

    full_text = ""
    return full_text

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