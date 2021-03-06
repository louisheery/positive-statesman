from django.contrib import admin

from .models import Article, Publisher, Category, Image, Location, Reader


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'publish_date',
                    'sentiment_score', 'user_score', 'user_score_count')
    list_filter = ['id']
    search_fields = ['title', 'id']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_filter = ['name']
    search_fields = ['name']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('creation_date', 'url', 'article')
    list_filter = ['creation_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'taxonomy_id')
    list_filter = ['name']
    search_fields = ['name']


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type')
    list_filter = ['name']
    search_fields = ['name']

class ReaderAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Reader, ReaderAdmin)
