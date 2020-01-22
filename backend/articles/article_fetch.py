#############################################################################
# Title:    Basic Script for Text Fetching and Sentiment Analysis           #
# Author:   ms519                                                           #
# Date:     22/01/2020                                                      #
#############################################################################

# In the requirements.txt   -> pip3 install vaderSentiment
#                           -> pip3 install newsapi-python 

# TODO:
# - Functions:
#   - generate_articles()
#   - fetch_metadata()
#   - get_full_text()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
import models

# Description:  Function to fetch and create Article Models
# Input:        none
# Output:       none

def generate_articles():
    
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

        p = models.Article(s_score)
        p.save

# Description:  Function to fetch article meta data from news api
# Input:        none
# Output:       list of metadata

def fetch_metadata(key):
    a = []
    return a

# Description:  Function to fetch the full text as a string
# Input:        link as string
# Output:       full text as string

def get_full_text(link):
    full_text = "lol"
    return full_text

# Description:  Function to calculate the compound Vader Score of a String
# Input:        text as string
# Output:       compund scores of the string

def sentiment_score(analyser,text):
    scores = analyser.polarity_scores(text)
    return scores['compound']


