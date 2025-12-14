from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Tag
from .serializers import PostSerializer, CommentSerializer, TagSerializer

@api_view(['GET'])
def api_overview(request):
    api_url = {
        'home': '/',
        'view_post': 'posts/',
        'search by tag': 'posts/?tag = tag name',
        'search by title': 'posts/?title = title name',
        'create_post': 'posts/create/',
        'update_post': 'posts/update/<slug>/',
        'delete_post': 'posts/delete/<slug>/',
        'create_comment': 'comments/create/',
        'view_post_comment': 'comments/post/<slug>/',
        'update_comment': 'comments/post/<slug>/update/<pk>/',
        'delete_comment': 'comments/post/<slug>/delete/<pk>/',
        'display_tags': 'tags/all/',
        'Login': 'account/login/',
        'logout': 'account/logout/',
        'register': 'account/register/',
        'token_refresh': 'account/token/refresh/',
    }
    return Response(api_url)

# POST
@api_view(['POST'])
def create_post(request):
    blog = PostSerializer(data=request.data)

    if Post.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This Post already Exists")
    
    if blog.is_valid():
        blog.save()
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_post(request):
    if request.query_params:
        blog = Post.objects.filter(**request.query_params.dict())
    else:
        blog = Post.objects.all()

    if blog:
        serializer = PostSerializer(blog, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_post(request, slug):
    blog = get_object_or_404(Post, slug=slug)

    if blog.author_id == request.user:
        serializer = PostSerializer(instance=blog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE'])
def delete_post(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    if blog.author_id == request.user:
        blog.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

# COMMENTS
@api_view(['POST'])
def create_comment(request):
    comment = CommentSerializer(data=request.data)

    if Comment.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This Comment already Exists")
    
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_post_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(post_id=post.pk)

    if comment:
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_comment(request, slug, pk):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(post_id=post.pk).get(pk=pk)

    if comment:
        if comment.user_id == request.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_comment(request, slug, pk):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(post_id=post.pk).get(pk=pk)

    if comment.user_id == request.user:
        comment.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
# TAG
@api_view(['GET'])
def display_tags(request):
    tags = Tag.objects.all()

    if tags:
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)