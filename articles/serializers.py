from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'url', 'image_url', 'publisher', 'publish_date', 'sentiment_score', 'text_snippet', 'text_full', 'score_user_numerator', 'score_user_denominator', 'categories']