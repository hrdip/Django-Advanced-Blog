from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# description of serializers
# in rest_framework we have response instead of HttpResponse meaning rest_framework loads only data not rendering pages
# serializer looks like context in the rendering page transforms data from model to json or xml like dictionary-style and returns to page with a response
# serializer and ModelSerializer similar to Django Forms and ModelForm, sometimes time no need for the model (Form) and sometimes we can use some fields or hole of "models" fields (ModelForm) to get data from users

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

    # we can overwrite fields from model for change to readonly serializers
    # If we choose read-only we can see this field but we can't change or update this field
    # author = serializers.ReadOnlyField()
    # author = serializers.CharField(read_only=True)

    # show part of content, this function (get_snippet) written in the model of this class
    # this function does not depend on request object, then we must write in models
    snippet = serializers.ReadOnlyField(source="get_snippet")
    # this function (get_absolute_api_url) written in the model of this class
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)

    # SerializerMethodField inside of serializer search for this method
    # look for (get_ + absolute_url) are belong to this field
    absolute_url = serializers.SerializerMethodField()

    # if we use category field come from model, the problem is when method=get only show id of category.

    # overwrite category field for get name instead of id. this is for relation fields (ManyToMany or ForeignKey)
    # category = serializers.SLugRelatedField(many=False, slug_field='name', queryset=Category.objects.all()) --> the problem is when method=post only get name of category not id

    # with this field we make object with CategorySerializer class. but the problem is when method=post for create post they didn't show list of categories
    # category = CategorySerializer()

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

        # another method for change field to read_only
        read_only_fields = ["author"]

    # if the function was dependent on request object, we must write the function in the serializer
    # if we didn't set the method_name for SerializerMethodField attribute, by default look for get_ at the beginning of the name field
    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    # we want when method=post we can see list of categories and we can send category by id like before, but for show to user we can show the name and id of category.
    # with this function even we can choose which fields are shown in the list view and which ones are shown in  the detail view
    # by checking the ID though the key=kwargs, it distinguishes between PostList and PostDetail
    def to_representation(self, instance):
        # get request items( before we said if we want written function base on request we must write in serializers.py instead of models.py)
        request = self.context.get("request")
        rep = super().to_representation(instance)

        # one of the items in request, in kwargs of parser_context we have pk then we know we used pk for detail view
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        # when we call CategorySerializer(means other serializer into the other serializer) it's much better send request object too
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        rep["author"] = AuthorSerializer(
            instance.author, context={"request": request}
        ).data
        return rep

    # the author is selected automatically based on user are authenticated
    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
