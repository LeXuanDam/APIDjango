from post.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage

class PostViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Post.objects.all().filter(id__lte=4)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        link_file = uploadFile(request.FILES['file'])
        request.data["file"] = link_file
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        post = checkPostExists(pk)
        if post == None:
            response = {"message": "post not exists"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        print(request)
        link_file = uploadFile(request.FILES['file'])
        request.data["file"] = link_file
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = checkPostExists(pk)
        if post==None:
            response = {"message": "post not exists"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        post = checkPostExists(pk)
        if post == None:
            response = {"message": "post not exists"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        response = {"message": "bạn đã xóa thành công post id = " + str(pk)}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


def uploadFile(uploaded_file):
    file = FileSystemStorage()
    name = file.save(uploaded_file.name, uploaded_file)
    return name
def checkPostExists(pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        post = None
    return post