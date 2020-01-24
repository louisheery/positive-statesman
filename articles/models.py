from django.db import models
from django import utils

class Article(models.Model):
    creation_date = models.DateTimeField(default=utils.timezone.now)
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=utils.timezone.now)
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT, null=True)
    categories = models.ManyToManyField('Category', blank=True)
    text_snippet = models.CharField(max_length=500)
    text_full = models.TextField(default='') # it makes sense to store the full text (at least in the beginning) since we can only use aylien API 1000 times per day. So if we change our NLP algorithm we can directly test and compare it to the old version without needing to waste our aylien API calls.
    score_model = models.FloatField(null=True)
    score_user_numerator = models.IntegerField(default=0)
    score_user_denominator = models.IntegerField(default=0)
    def score_user(self):
        return self.score_user_numerator / self.score_user_denominator
    class Meta:
        ordering = ['creation_date']

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, null=True)
    class Meta:
        ordering = ['name']

class Image(models.Model):
    creation_date = models.DateTimeField(default=utils.timezone.now)
    url = models.URLField(max_length=200)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['creation_date']

class Category(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField('Article', blank=True)
    class Meta:
        ordering = ['name']
