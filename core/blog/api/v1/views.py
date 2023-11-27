from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from ... models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins


# Example for Function Based View
'''
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
   '''     

'''
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
        return Response({"detail" : " Item removed successfully"}, status=status.HTTP_204_NO_CONTENT )  
    '''    


# Example For Class Base view for APIView
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
        return Response({"detail" : " Item removed successfully"}, status=status.HTTP_204_NO_CONTENT )  
    '''


# Example-PostList (1) For Class Base view for GenerciView only
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


# Example-PostList (3) For Class Base view for ListCreateAPIView
# Best one
class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# Example-PostDetail (1) For Class Base view for GenerciView only
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
        return Response({"detail" : " Item removed successfully"}, status=status.HTTP_204_NO_CONTENT ) 
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
        return self.destroy(request, *args, **kwargs) 
    ''' 

# Example-PostDetail (3) For Class Base view for RetrieveUpdateDestroyAPIView
# Best one
class PostDetail(RetrieveUpdateDestroyAPIView):
    """ gettinf detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    lookup_field = 'id'
    