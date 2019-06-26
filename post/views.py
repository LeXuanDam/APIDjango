from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post, Author, Category
from post.serializers import PostSerializer, CategorySerializer, AuthorSerializer
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import json

@api_view(['GET', 'POST'])

def list(request):
    """
    List all code posts, or create a new post.
    """

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        link_file = uploadFile(request.FILES['file'])
        request.data["file"] = link_file
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
        return Response(post.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
    """
    Retrieve, update or delete a code post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        response = {"message": "post not exists"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        request = uploadFile(request)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        respone = {"message": "bạn đã xóa thành công bài post id = " + str(pk)}
        return Response(respone, status=status.HTTP_204_NO_CONTENT)

def uploadFile(uploaded_file):
    file = FileSystemStorage()
    name = file.save(uploaded_file.name, uploaded_file)
    return name