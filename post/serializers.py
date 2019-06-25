from rest_framework import serializers
from post.models import Post, Category, Author

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, default='')
    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, default='')
    # email = serializers.CharField(max_length=100, default='')
    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        # instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    file = serializers.CharField(max_length=100, default='')
    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
class GetPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    file = serializers.CharField(max_length=100, default='')
    category = CategorySerializer()
    author = AuthorSerializer()