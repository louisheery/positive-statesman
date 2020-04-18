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

#For tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

#Tensorflow
import tensorflow as tf
tf.get_logger().setLevel('INFO')
import tensorflow_hub as hub
import numpy as np
from tensorflow.contrib import predictor

#BERT
import bert
from bert import run_classifier
from bert import tokenization
import os

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

    #Load sentiment model
    #vader_analyser = SentimentIntensityAnalyzer()
    bert_predictor = load_bert_predictor(os.getcwd() + '/articles/bert_model')

    # 1.    Fetch articles

    api_response = fetch_articles(api_instance)
    stories = api_response.stories
    # TBD error handling

    # 2.    Get the full text for every article
    # 2.1       Analyse sentiment
    for story in stories:
        save_from_story(story, bert_predictor)
        
def fetch_articles(api_instance):
    try:
        api_response = api_instance.list_stories(
            published_at_start='NOW-1DAYS',
            published_at_end='NOW',
            per_page=1,
            categories_taxonomy='iab-qag',
            categories_id=['IAB1', 'IAB3', 'IAB11', 'IAB15', 'IAB17', 'IAB19', 'IAB20'],
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

    # scores = analyser.polarity_scores(text)
    # return scores['compound']
    return split_and_predict(text, analyser)


def save_from_story(story, predictor):
    title = story.title
    publish_date = story.published_at
    url = story.links.permalink
    publisher = Publisher.objects.get_or_create(name=story.source.name)[0]
    image_url = ''
    for media in story.media:
        if (media.type == 'image'):
            image_url = media.url
    full_text = story.body

    s_score = sentiment_score(predictor, full_text)

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


###BERT FUNCTIONS###
def create_tokenizer_from_hub_module():
    # This is a path to an uncased (all lowercase) version of BERT
    BERT_MODEL_HUB = "https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1"

    """Get the vocab file and casing info from the Hub module."""
    with tf.Graph().as_default():
        bert_module = hub.Module(BERT_MODEL_HUB)
        tokenization_info = bert_module(signature="tokenization_info", as_dict=True)
        with tf.Session() as sess:
            vocab_file, do_lower_case = sess.run([tokenization_info["vocab_file"],
                                                tokenization_info["do_lower_case"]])
        
    return bert.tokenization.FullTokenizer(
        vocab_file=vocab_file, do_lower_case=do_lower_case)

def convert_for_bert(sentence):
    
    label_list = [0, 1]
    tokenizer = create_tokenizer_from_hub_module()

    # Transformation into BERT input features
    input_examples = [run_classifier.InputExample(guid="", text_a=sentence, text_b=None,label=0)]
    input_features = run_classifier.convert_examples_to_features(input_examples, label_list, 128, tokenizer)

    input_ids = np.array(input_features[0].input_ids)
    segment_ids = np.array(input_features[0].segment_ids)
    input_masks = np.array(input_features[0].input_mask)
    label_ids = np.array(input_features[0].label_id)

    # Needs to be in dictionary format for prediction function
    tensor_dict = {"label_ids": [label_ids.tolist()], "segment_ids": [segment_ids.tolist()],"input_mask":[input_masks.tolist()],"input_ids": [input_ids.tolist()]}

    # Only required for serving
    # import json
    # data_dict = {"inputs": tensor_dict}
    # data = json.dumps(data_dict) 

    return tensor_dict

def load_bert_predictor(directory):
    predict_fn = tf.contrib.predictor.from_saved_model(directory)
    return predict_fn

def positivity_score(probability):
    return probability[0][0] / np.sum(probability[0])

def convert_probabilities_to_labels(probability):
  threshold = 0.5
  
  if probability > threshold:
    return 1
  else:
    return 0

def split_and_predict(text, predict_fn):
    #Split into sentences
    sentences = sent_tokenize(text)

    #for each sentence, put the positivity score into an array
    predictions = [positivity_score(predict_fn(convert_for_bert(sentence))['probabilities']) for sentence in sentences]
    
    #Calculate average sentiment score  
    average_sentiment_score = sum(predictions) / len(predictions)
    print(text)
    print(f'AVERAGE SENTIMENT SCORE: {average_sentiment_score}')
    return average_sentiment_score
####################

############################## FUNCTION TESTING ###############################

# TEST: fetch_metadata(...)

# TEST: get_full_text(...)

# TEST: sentiment_score(...)

# sentiment_analyser = SentimentIntensityAnalyzer()
# sample_text = "Hospitals in the Chinese city of Wuhan have been \
#  thrown into chaos and the movement of about 33 million people has been \
#     restricted by an unprecedented and indefinite lockdown imposed to halt the \
#         spread of the deadly new coronavirus. At least 10 cities in central \
#             Hubei province have been shut down in an effort to stop the virus, \
#                 which by Friday had killed 26 people across China and affected \
#                     more than 800. The World Health Organisation described the \
#                         outbreak as an emergency for China, but stopped short \
#                             of declaring it to be a public health emergency of \
#                                 international concern."

# print("Compound Sentiment Score: ", sentiment_score(sentiment_analyser, sample_text))

# TEST: generate_articles(...)

################################# DRIVER CODE #################################

#generate_articles()

