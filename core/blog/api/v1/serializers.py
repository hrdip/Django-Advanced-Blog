from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# model for Serializer
"""
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    """


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "first_name")
        model = Profile


# model for ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    # category = serializers.SLugRelatedField(many=False, slug_field='name', queryset=Category.objects.all()) --> only category names are shown
    # category = CategorySerializer()--> problem: only the category ID is taken and not the category name

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "content",
            "category",
            "status",
            "snippet",
            "relative_url",
            "absolute_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri()

    # the category id and category name are shown but for post creations only category name is taken
    """
    def to_representation(self, instance): 
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
    """

    # all categories problem are fixed
    # by checking the ID though the key=kwargs, it distinguishes between PostList and PostDetail
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        rep["author"] = AuthorSerializer(instance.author).data
        return rep

    # the author is selected automatically based on user
    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
