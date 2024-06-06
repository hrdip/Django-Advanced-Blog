from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"

# in viewsets because we need to map functions,  this router handles this automatically
# in DefaultRouter base on viewsets functionality generated automatically urls
# make object with DefaultRouter class
router = DefaultRouter()
# use method of DefaultRouter class
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
# add routers are generated to urlpatterns
urlpatterns = router.urls

"""
urlpatterns = [
    # FBV,
    # path('post/', views.postList, name='post-list'),
    # path('post/<int:id>', views.postDetail, name='post-detail'),
    # APIView and GenericView,
    # path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    # ViewSet,
    path('post/', views.PostViewSet.as_view({'get':'list', 'post':'crate'}), name='post-list'),
    path('post/<int:pk>', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-detail'),
]
"""
