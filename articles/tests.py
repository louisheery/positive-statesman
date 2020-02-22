from .models import Article, Publisher, Location, Category, Image
from django.test import TestCase
from django.utils import timezone


# Model Tests
class ModelTest(TestCase):

    def create_Article(self):
        return Article.objects.create()

    def test_article_functions(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing Article Model ...")
        print("----------------------------------------------------------------------")
        a = self.create_Article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.user_score(), 0)
        self.assertEqual(a.__str__(), "")
        print("OK")

    def create_Publisher(self):
        return Publisher.objects.create()

    def test_publisher_functions(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing Publisher Model ...")
        print("----------------------------------------------------------------------")
        a = self.create_Publisher()
        self.assertTrue(isinstance(a, Publisher))
        self.assertEqual(a.__str__(), "")
        print("OK")

    def create_Image(self):
        return Image.objects.create()

    def test_image_functions(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing Image Model ...")
        print("----------------------------------------------------------------------")
        a = self.create_Image()
        self.assertTrue(isinstance(a, Image))
        self.assertEqual(a.__str__(), "")
        print("OK")