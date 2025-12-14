from django.db.models import fields
from rest_framework import serializers
from .models import Tag, Post, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'title', 'slug', 'content', 'votes', 'tag', 'author_id', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'author_name', 'author_email', 'user_id', 'content', 'created_at')