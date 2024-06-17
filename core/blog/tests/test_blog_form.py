from django.test import TestCase
from ..forms import PostForm
from datetime import datetime
from ..models import Category


# for testing forms, need to send some data to check the validation
class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        # many to many fields created like below and category are saved in the database then we need TestCase
        category_obj = Category.objects.create(
            name='Hello'
        )
        # send required data to PostForm
        form = PostForm(data={
            "title": "test",
            "content": "descriptions",
            "status": True,
            "category": category_obj,
            "published_date": datetime.now()
        })
        # check True or not
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        # check False or not
        self.assertFalse(form.is_valid())
