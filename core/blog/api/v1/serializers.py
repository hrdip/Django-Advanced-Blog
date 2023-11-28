from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile



# model for Serializer
'''
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    '''

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name')
        model = Profile

# model doe ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    #content = serializers.ReadOnlyField()
    #content =serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    #category = serializers.SLugRelatedField(many=False, slug_field='name', queryset=Category.objects.all()) --> just show name
    #category = CategorySerializer()--> cant chose category by id
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'title', 'content', 'category', 'status','snippet', 'relative_url', 'absolute_url', 'created_date', 'published_date']
        read_only_fields = ['author']
 
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri()
    
    # Fix problems of Category (show id and name, and for create just get id but show name)
    '''
    def to_representation(self, instance): 
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
    '''

    # Fix problems of Category and separated  PostList fields and DetailList fields by checking id with keyname= kwargs
    def to_representation(self, instance): 
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else: 
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        rep['author'] = AuthorSerializer(instance.author).data
        return rep 
    
    # select automatically author for user login
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
