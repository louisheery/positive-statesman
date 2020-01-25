from django.core.management.base import BaseCommand
from articles.article_fetch import generate_articles

class Command(BaseCommand):
    help = 'Populates database with new articles'

    def handle(self, *args, **kwargs):
        generate_articles()