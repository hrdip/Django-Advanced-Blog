from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category
from datetime import datetime


# request to the URL to check whether this URL returns a view or not
class TestBlogViews(TestCase):

    def setUp(self):
        # handling send request with python
        self.client = Client()
        self.user = User.objects.create_user(
            email='user@example.com',
            password='a/@1234567'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test_name",
            last_name="test_last_name",
            description="test description"
        )
        self.category_obj = Category.objects.create(
            name='Hello'
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="descriptions",
            status=True,
            category=self.category_obj,
            published_date=datetime.now()
        )

    def test_blog_index_url_successful_response(self):
        url = reverse('blog:fbv-index')
        # send request with client object
        response = self.client.get(url)
        # check when we request, return the correct response
        self.assertEqual(response.status_code, 200)
        # checking if the content contains this word or not
        self.assertTrue(str(response.content).find("hossein"))
        # check this view return this template or not
        self.assertTemplateUsed(response, template_name="index.html")

    # testing login required  views
    def test_blog_post_detail_logged_in_response(self):
        # login user with force_login
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        # check when we request, return the correct response
        self.assertEqual(response.status_code, 200)

    # testing views login required, with logout user
    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
