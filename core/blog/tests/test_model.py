from django.test import TestCase 
from datetime import datetime
from ..models import Post
from accounts.models import User, Profile

# Create your tests here.
class TestPostModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='a/@1234567')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = "test_name",
            last_name = "test_last_name",
            description = "test description"
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "descriptios",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, 'test')
      
