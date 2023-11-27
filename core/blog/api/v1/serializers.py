from rest_framework import serializers
from ...models import Post, Category



# model for Serializer
'''
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    '''

# model doe ModelSerializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'category', 'status', 'created_date', 'published_date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']