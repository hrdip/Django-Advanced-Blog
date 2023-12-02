from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import homeView

# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_website_index_url_resolve(self):
        url = reverse('website:home')
        self.assertEqual(resolve(url).func,homeView)