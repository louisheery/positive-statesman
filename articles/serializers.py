from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    publisher = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Article
        fields = ['id', 'title', 'url', 'image_url', 'publisher', 'publish_date', 'sentiment_score', 'user_score_positive', 'user_score_neutral', 'user_score_negative', 'user_score_count', 'categories', 'locations', 'creation_date']
