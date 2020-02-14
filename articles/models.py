from django.db import models
from django import utils


class Article(models.Model):
    creation_date = models.DateTimeField(default=utils.timezone.now)
    url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=utils.timezone.now)
    publisher = models.ForeignKey(
        'Publisher', on_delete=models.PROTECT, null=True)
    categories = models.ManyToManyField('Category', blank=True)
    locations = models.ManyToManyField('Location', blank=True)
    text_snippet = models.CharField(max_length=500, default='')
    text_full = models.TextField(default='')
    sentiment_score = models.FloatField(null=True)
    user_score_positive = models.IntegerField(default=0)
    user_score_neutral = models.IntegerField(default=0)
    user_score_negative = models.IntegerField(default=0)
    user_score_count = models.IntegerField(default=0)

    def user_score(self):
        return 0 if self.user_score_count == 0 \
            else (self.user_score_positive * 1 + self.user_score_neutral * 0 + \
                self.user_score_negative * -1) / self.user_score_count

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['creation_date']


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Image(models.Model):
    creation_date = models.DateTimeField(default=utils.timezone.now)
    url = models.URLField(max_length=200)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['creation_date']


class Category(models.Model):
    name = models.CharField(max_length=100)
    taxonomy_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Location(models.Model):
    name = models.CharField(max_length=100, null=True)
    location_type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
