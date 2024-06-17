from django.test import TestCase
from django.urls import reverse, resolve
from ..views import PostListView, PostDetailView, IndexView


# simpleTestCase is not related to the database, like checking the URL are connected to the class
# post data for testing handling forms, not for saving data on the database

# TransactionTestCase used for testing based on the database, like created models and save data on it
# the operating on the main database and after finishing jobs, delete all. the problem is takes time too much

# TestCase used for testing based on the dummy database and after finish testing delete database. more simple and faster than TransactionTestCase


# class name must be started with Test
# function name must be started with test
# file name must be started with test
# for running a TestCase used this code (python manage.py test)
class TestUrl(TestCase):

    def test_blog_index_url_resolve(self):
        url = reverse("blog:cbv-index")
        # we have too many assert checking
        # test whether this URL belongs to this class or not. if we used fbv no need to add the view_class method
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post-list")
        # we have too many assert checking
        # test whether this URL belongs to this class or not. if we used fbv no need to add the view_class method
        self.assertEquals(resolve(url).func.view_class, PostListView)

    # sending parameter for url like detail view
    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={'pk': 1})
        # we have too many assert checking
        # test whether this URL belongs to this class or not. if we used fbv no need to add the view_class method
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
