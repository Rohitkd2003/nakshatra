from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # read-only user

    class Meta:
        model = Post
        fields = ["id", "user", "text", "created_at"]

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # read-only user
    post = serializers.PrimaryKeyRelatedField(read_only=True)  # post assigned in view

    class Meta:
        model = Comment
        fields = ["id", "post", "user", "comment", "created_at"]
