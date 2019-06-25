from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import json


@api_view(['GET', 'POST'])

def list(request):
    """
    List all code category, or create a new category.
    """

    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(category.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
    """
    Retrieve, update or delete a code category.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        response = {"message": "category not exists"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        response = {"message": "bạn đã xóa thành công category id = " + str(pk)}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
