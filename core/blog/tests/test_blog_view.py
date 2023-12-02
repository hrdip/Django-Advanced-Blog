from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile  
from blog.models import Post, Category 
from datetime import datetime
# Create your tests here.
class TestBlogViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='user@example.com', password='a/@1234567')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = "test_name",
            last_name = "test_last_name",
            description = "test description"
        )
        self.post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "descriptios",
            status = True,
            category = None,
            published_date = datetime.now()
        )

    def test_blog_index_url_succesful_response(self):
        url = reverse('blog:fbv-index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("hossein"))
        self.assertTemplateUsed(response,template_name="index.html")
 
    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
         
    def test_blog_post_detail_anonymouse_response(self):
        url = reverse('blog:post-detail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)