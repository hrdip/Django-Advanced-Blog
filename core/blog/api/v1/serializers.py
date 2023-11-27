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
    #content = serializers.ReadOnlyField()
    #content =serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'category', 'status','snippet', 'relative_url', 'absolute_url', 'created_date', 'published_date']
        #read_only_fields = ['content']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri()



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']