from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from accounts.models import User, Profile


# testing create object in model
class TestPostModel(TestCase):

    # create user and profile object for creating post object generally, then used in other functions
    # function for creating inputs object
    def setUp(self):
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

    def test_create_post_with_valid_data(self):
        # create post object with data
        post = Post.objects.create(
            # for creating post we need to have author
            author=self.profile,
            title="test",
            content="descriptions",
            status=True,
            category=self.category_obj,
            published_date=datetime.now()
        )
        # check post object is created or not
        # post.id belongs to  the post object we have created now
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        # check post object title equal 'test' or not
        self.assertEqual(post.title, 'test')
