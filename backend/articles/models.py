from django.db import models
from datetime import datetime

class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256, default='')
    publisher = models.CharField(max_length=30, default='')
    publish_date = models.DateTimeField(default=datetime.now())
    sentiment_score = models.IntegerField(default=0)

    class Meta:
        ordering = ['created']

    @classmethod
    def create(cls, created, title, url, image_url, publisher, publish_date, sentiment_score):
        article = cls(created=created, title=title, url=url, image_url=image_url, publish_date=publish_date,publisher=publisher,sentiment_score=sentiment_score)
        return article
