from .models import Article, Publisher, Location, Category, Image, User, Reader
import articles.article_fetch as af
import articles.views as av
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import django.http as http
from django.test import Client
import requests
import json
#from django.utils import unittest
from django.test.client import RequestFactory
from django.contrib import auth


#from .views import article_average

# Model Tests
class ModelTest(TestCase):

    def create_Article(self):
        return Article.objects.create()

    '''
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

# Script Function Tests
class ScriptTest(TestCase):

    def test_generate_article(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing generate_article() Function ...")
        print("----------------------------------------------------------------------")
        try:
            af.generate_articles()
        except Exception as e:
            self.fail("Unexpected exception %s" % e) 

    def test_save_article(self):
        url = 'https://www.faz.net/aktuell/politik/wahl-in-hamburg/wahl-in-hamburg-eine-stadt-waehlt-sich-selbst-16646792.html'
        
        print("")
        print("----------------------------------------------------------------------")
        print("Testing save_article() Function...")
        print("----------------------------------------------------------------------")
        try:
            af.save_article(url)
        except Exception as e:
            self.fail("Unexpected exception %s" % e) 

# View Tests
class ViewTest(TestCase):

    def test_valid_filter(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing valid_filter() Function ...")
        print("----------------------------------------------------------------------")
        param_true = 'u'
        param_false = ''
        self.assertTrue(av.valid_filter(param_true))
        self.assertTrue(not av.valid_filter(param_false))

    def test_article_filter(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the article_filter() View ...")
        print("----------------------------------------------------------------------")
        request = http.HttpRequest()
        request.method = 'GET'
        request.GET = http.QueryDict('category=politcs')

        try:
            qset = av.article_filter(request)
        except Exception as e:
            self.fail("Unexpected exception %s" % e) 
        c = Client()
        response = c.post('/api/submit-article/', {'url': 'http://pornhub.com'})
        response.status_code

    def test_fetch_article(self):
        c = Client()
        print("")
        print("----------------------------------------------------------------------")
        print("Testing fetch_article() View ...")
        print("----------------------------------------------------------------------")

        post_data = {'name': 'Gladys'}
        response = c.get('api/fetch-articles/')
        content = response.status_code
        print(content)

    def test_submit_article(self):

        print("")
        print("----------------------------------------------------------------------")
        print("Testing submit_article() View ...")
        print("----------------------------------------------------------------------")

        c = Client()
        url = 'https://www.faz.net/aktuell/politik/wahl-in-hamburg/wahl-in-hamburg-eine-stadt-waehlt-sich-selbst-16646792.html'
        
        python_dict = {
        'body': {
            'url': url
            }
        }
        
        response = c.post('/api/submit-article/',
                                json.dumps(python_dict),
                                content_type="application/json")

        self.assertEqual(response.status_code, 404)

    def test_article_detail(self):

        print("")
        print("----------------------------------------------------------------------")
        print("Testing the article_detail() View ...")
        print("----------------------------------------------------------------------")
        Article.objects.create()
        Article.objects.create()
        request = http.HttpRequest()
        request.method = 'GET'
        request.GET = http.QueryDict('category=politcs')

        try:
            qset = av.article_detail(request, 1)
        except Exception as e:
            self.fail("Unexpected exception %s" % e) 

    def test_user_feedback(self):

        print("")
        print("----------------------------------------------------------------------")
        print("Testing the user_feedback() Function ...")
        print("----------------------------------------------------------------------")
        Article.objects.create()
        Article.objects.create()
        request = http.HttpRequest()
        request.method = 'GET'
        request.GET = http.QueryDict('category=politcs')

        try:
            qset = av.user_feedback(request, 1, "positive")
        except Exception as e:
            self.fail("Unexpected exception %s" % e) 

    '''

    def test_login(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the login() Function ...")
        print("----------------------------------------------------------------------")
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        python_dict = {
            'username': 'temporary',
            'password': 'temporary'
        }
        c = Client()
        response = c.post('/api/login/',
                                json.dumps(python_dict),
                                content_type="application/json")
        user = auth.get_user(c)
        self.assertTrue(user.is_authenticated)

    def loginSampleUser(self):
        '''
        Create sample user and log in - utility function for other tests
        '''
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        reader = Reader(user=user)
        reader.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        return c

    def test_logout(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the logout() Function ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        response = c.post('/api/logout/',
                                json.dumps({}),
                                content_type="application/json")
        user = auth.get_user(c)
        self.assertTrue(not user.is_authenticated)


    def test_signup(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the signup() Function ...")
        print("----------------------------------------------------------------------")
        python_dict = {
            'username': 'temporary',
            'password': 'temporary',
            'email': 'temporary@gmail.com'
        }
        c = Client()
        response = c.post('/api/signup/',
                                json.dumps(python_dict),
                                content_type="application/json")
        user = auth.get_user(c)
        self.assertTrue(user.is_authenticated)


    def test_auth_popular_publisher(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the Auth Guard for setting publisher preferences ...")
        print("----------------------------------------------------------------------")
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        publisher = Publisher.objects.create(name="testpublisher")
        python_dict = {
            'name': 'testpublisher'
        }
        c = Client()
        response = c.post('/api/popular/publisher/', json.dumps(python_dict), content_type="application/json")
        self.assertEqual(response.status_code, 500)


    def test_add_popular_publisher(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the adding of popular publisher ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testpublisher"
        publisher = Publisher.objects.create(name=sampleName)
        python_dict = {
            'name': sampleName
        }
        response = c.post('/api/popular/publisher/', json.dumps(python_dict), content_type="application/json")
        user = auth.get_user(c)
        self.assertTrue(user.reader.publishers.filter(name=sampleName).exists())


    def test_remove_popular_publisher(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the remove of popular publisher ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testpublisher"
        publisher = Publisher.objects.create(name=sampleName)
        python_dict = {
            'name': sampleName
        }
        user = auth.get_user(c)

        user.reader.publishers.add(publisher)
        self.assertTrue(user.reader.publishers.filter(name=sampleName).exists())

        response = c.delete('/api/popular/publisher/', json.dumps(python_dict), content_type="application/json")
        self.assertTrue(not user.reader.publishers.filter(name=sampleName).exists())


    def test_get_popular_publisher(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the getting of popular publisher ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testpublisher"
        publisher = Publisher.objects.create(name=sampleName)
        python_dict = {
            'name': sampleName
        }
        user = auth.get_user(c)
        user.reader.publishers.add(publisher)
        response = c.get('/api/popular/publisher/', content_type="application/json")
        self.assertTrue(sampleName in [publisher["name"] for publisher in response.json()['info']])



    def test_auth_popular_category(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the Auth Guard for setting category preferences ...")
        print("----------------------------------------------------------------------")
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        sampleName = "testCategory"
        taxonomy_id = "testid"
        publisher = Category.objects.create(name=sampleName,taxonomy_id=taxonomy_id)
        python_dict = {
            'id': taxonomy_id
        }
        c = Client()
        response = c.post('/api/popular/category/', json.dumps(python_dict), content_type="application/json")
        self.assertEqual(response.status_code, 500)


    def test_add_popular_category(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the adding of popular category ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testCategory"
        taxonomy_id = "testid"
        publisher = Category.objects.create(name=sampleName,taxonomy_id=taxonomy_id)
        python_dict = {
            'id': taxonomy_id
        }
        response = c.post('/api/popular/category/', json.dumps(python_dict), content_type="application/json")
        user = auth.get_user(c)
        self.assertTrue(user.reader.categories.filter(name=sampleName).exists())


    def test_remove_popular_category(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the remove of popular category ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testCategory"
        taxonomy_id = "testid"
        category = Category.objects.create(name=sampleName,taxonomy_id=taxonomy_id)
        python_dict = {
            'id': taxonomy_id
        }
        user = auth.get_user(c)

        user.reader.categories.add(category)
        self.assertTrue(user.reader.categories.filter(name=sampleName).exists())

        response = c.delete('/api/popular/category/', json.dumps(python_dict), content_type="application/json")
        self.assertTrue(not user.reader.categories.filter(name=sampleName).exists())


    def test_get_popular_category(self):
        print("")
        print("----------------------------------------------------------------------")
        print("Testing the getting of popular category ...")
        print("----------------------------------------------------------------------")
        c = self.loginSampleUser()
        sampleName = "testCategory"
        taxonomy_id = "testid"
        category = Category.objects.create(name=sampleName,taxonomy_id=taxonomy_id)
        python_dict = {
            'id': taxonomy_id
        }
        user = auth.get_user(c)
        user.reader.categories.add(category)
        response = c.get('/api/popular/category/', content_type="application/json")
        self.assertTrue(sampleName in [category["name"] for category in response.json()['info']])

    

""" class RequestTest(TestCase):
from django.utils import unittest
from django.test.client import RequestFactory

from .views import article_average
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/analytics')

        response = article_average(request)

        print(response)

        self.assertEqual(response.status_code, 200) """
