from rest_framework import serializers
from rest_framework.response import Response

from posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
    like = serializers.IntegerField(default=0, read_only=True)
    view = serializers.IntegerField(default=0, read_only=True)
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)

        return post
# class PostRetrieveSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     tags = serializers.StringRelatedField(many=True)
    
#     class Meta:
#         model = Post
#         fields = '__all__'  

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'