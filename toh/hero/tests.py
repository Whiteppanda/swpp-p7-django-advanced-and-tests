from http import client
from pydoc import cli
from urllib import response
from django.test import TestCase, Client
from .models import Hero

# Create your tests here.
class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name="Superman")
        Hero.objects.create(name="Batman")
        Hero.objects.create(name="Ironman")
        
    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)
        
    def test_hero_id(self):
        client = Client()
        response = client.get('/hero/10/')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('10', response.content.decode())
        
    def test_hero_page(self):
        client = Client()
        response = client.get('/hero/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.content.decode())
        response = client.get('/hero/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('2', response.content.decode())

