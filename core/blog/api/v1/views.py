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
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination, CustomPagination


# 1) Function Base View
"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
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
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    """
# 2) Class Base View by APIView
'''
class PostList(APIView):
    """getting a list of posts and creating new posts"""

    permission_classes =  [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """retriving a list of posts"""
        posts = Post.objects.filter(status=True)
        # serializer = PostSerializer(posts,many=True)
        serializer = self.serializer_class(posts,many=True)
        return Response(serializer.data)
    def post(self, request):
        """creating a new post with provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   '''

'''
class PostDetail(APIView):
    """ gettinf detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retriveing the post data"""
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """editing the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        """deleting the post object"""
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    '''

# 3) Class Base View by GenericView
# Example (1) For Class Base view for GenerciView only
'''
class PostList(GenericAPIView):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request):
        """retriving a list of posts"""
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self, request):
        """creating a new post with provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    '''

'''
class PostDetail(GenericAPIView):
    """ gettinf detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retriveing the post data"""
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """editing the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        """deleting the post object"""
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    '''

# Example-PostList (2) For Class Base view for GenerciView with ListModelMixin and CreateModelMixin
'''
class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retriving a list of posts"""
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        """creating a new post with provided data"""
        return self.create(request, *args, **kwargs)
    '''

# Example-PostDetail (2) For Class Base view for GenerciView with RetrieveModelMixin, UpdateModelMixin and DestroyModelMixin
'''
class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """ gettinf detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """retriveing the post data"""
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        """editing the post data """
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        """deleting the post object"""
        return self.destroy(request,*args,**kwargs)
    '''


# Example-PostList (3) For Class Base view for ListCreateAPIView
# Best one
'''
class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    '''

# Example-PostDetail (3) For Class Base view for RetrieveUpdateDestroyAPIView
# Best one
'''
class PostDetail(RetrieveUpdateDestroyAPIView):
    """ gettinf detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    lookup_field = 'id'
    '''


# 3) Class Base View (ViewSet)
# Example for ViewSet in CBV
"""
class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def create(self,request):
        pass
    def update(self,request,pk=None):
        pass
    def partial_update(self,request,pk=None):
        pass
    def destroy(self,request,pk=None):
        pass
    """


# 4) Class Base View (ModelViewSet)
# Example for ModelViewSet in CBV
# The Best One
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
