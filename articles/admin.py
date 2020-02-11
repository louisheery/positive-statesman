from django.contrib import admin

from .models import Article, Publisher, Category, Image, Location

# Register your models here.

admin.site.register(Article)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)