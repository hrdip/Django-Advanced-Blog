from django.test import TestCase,SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import homeView

# Create your tests here.
class TestUrl(SimpleTestCase):
    def test_website_home_url_resolve(self):
        url = reverse('website:home')
        self.assertEqual(resolve(url).func,homeView)


# Create your tests here.
class TestWebsiteViews(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_website_home_url_succesful_response(self):
        url = reverse('website:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("welcome"))
        self.assertTemplateUsed(response,template_name="home.html")
 