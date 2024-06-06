from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination, CustomPagination


# 1) Function Base View
"""
# this decorator adds rest_framework structure to the function base view
@api_view(['GET', 'POST'])
# permission decorator most be come after api_view
@permission_classes([IsAuthenticatedOrReadOnly, IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        # transform item in input (post) to json with serializer
        serializer = PostSerializer(posts,many=True)
        # in rest_framework we have response instead of HttpResponse meaning rest_framework loads only data not rendering pages
        # serializer looks like context in the rendering page transforms data from model to json or xml like dictionary-style and returns to page with a response
        # serializer and ModelSerializer similar to Django Forms and ModelForm, sometimes time no need for the model and sometimes we can use some fields of models to get data from users
        return Response(serializer.data)
    # send data from user and save on database
    elif request.method == 'POST':
        # request.data is data come from user for fill up the forms
        serializer = PostSerializer(data=request.data)
        # check validation serializers
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   """

"""
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == 'GET':
        # transform item in input (post) to json with serializer
        serializer = PostSerializer(post)
        return Response(serializer.data)
    # update existing post
    elif request.method == 'PUT':
        # we use this code (data=request.data) to get the last data are save it on the database to update them
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    # delete existing post
    elif request.method == 'DELETE':
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    """

# 2) Class Base View by APIView
# first generations of class base view for rest_framework and give us HTML forms instead of fbv row form, and user can fill up very easily forms
'''
class PostList(APIView):
    """get a list of posts and create new posts"""

    permission_classes =  [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """retrieve a list of posts"""
        posts = Post.objects.filter(status=True)
        # serializer = PostSerializer(posts,many=True)
        serializer = self.serializer_class(posts,many=True)
        return Response(serializer.data)
    def post(self, request):
        """create a new post with the provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   '''

'''
class PostDetail(APIView):
    """ get details of the post and edit plus remove it"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retrieve the post data"""
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """update the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        """delete the post object"""
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    '''

# 3) Class Base View by GenericView
# GenericAPIView without mixins
# the second generation of CBV, have queryset for get the object from models or send our data for save on database with the model
# In APIView each method needs to get the object separately, but here one time we get the object and save it on queryset and use it in each method we need with self.queryset code
'''
class PostList(GenericAPIView):
    """get a list of posts and create new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request):
        """retrieve a list of posts"""
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self, request):
        """create a new post with the provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    '''

'''
class PostDetail(GenericAPIView):
    """ get details of the post and edit plus remove it"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, id):
        """retrieve the post data"""
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """edit the post data """
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        """delete the post object"""
        post = get_object_or_404(self.queryset, pk=pk)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    '''

# GenericAPIView with mixins
# in this class we dont have get, post, put and delete function, then we need call them and return list, create, retrieve, update and destroy function
'''
class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """get a list of posts and create new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieve a list of posts"""
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        """creating a new post with provided data"""
        return self.create(request, *args, **kwargs)
    '''

'''
class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """ get details of the post and edit plus remove it"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieve the post data"""
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        """edit the post data """
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        """delete the post object"""
        return self.destroy(request,*args,**kwargs)
    '''


# Class Base View by ListCreateAPIView, the kind of GenericAPIView mixed with GenericAPIView plus mixins.ListModelMixin plus mixins.CreateModelMixin for the list or create a post. in the mother class already have get and post methods and no need to overwrite them again
# ListAPIView and CreateAPIView class are exist and get list of post and create new post separately
'''
class PostList(ListCreateAPIView):
    """get a list of posts and create new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    '''

# Class Base View by RetrieveUpdateDestroyAPIView, the kind of GenericAPIView mixed with GenericAPIView plus mixins.RetrieveModelMixin plus mixins.UpdateModelMixin plus mixins.DestroyModelMixin for the retrieve or update or destroy a post. in the mother class already have get, put and delete methods and no need to overwrite them again
'''
class PostDetail(RetrieveUpdateDestroyAPIView):
    """ get details of the post and edit plus remove it"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    '''


# 4) Class Base View by ViewSet
# the 3rd generation of CBV, but function name are changed, get = list or retrieve, post = create, put = update, patch = partial_update and delete = destroy
'''
class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer = self.serializer_class(self.queryset)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def update(self,request,pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def partial_update(self,request,pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        post_object.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    '''


# 5) Class Base View by ModelViewSet
# this viewsets are generate all elements by models
# included all mixins classes in GenericAPIView
class PostModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact"],
    }
    search_fields = ["title", "$content", "=category__name"]
    ordering_fields = ["published_date"]
    pagination_class = CustomPagination


class CategoryModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
