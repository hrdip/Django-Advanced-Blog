from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"
router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
urlpatterns = router.urls

'''
urlpatterns = [
    # FBV,
    # path('post/', views.postList, name='post-list'),
    # path('post/<int:id>', views.postDetail, name='post-detail'),
    # APIView and GenericView,
    # path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:id>', views.PostDetail.as_view(), name='post-detail'),
    # ViewSet,
    path('post/', views.PostViewSet.as_view({'get':'list', 'post':'crate'}), name='post-list'),
    path('post/<int:pk>', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-detail'),
]
'''

 