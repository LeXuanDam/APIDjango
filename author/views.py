from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Author
from post.serializers import AuthorSerializer

@api_view(['GET', 'POST'])

def list(request):
    """
    List all code author, or create a new author.
    """

    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        author = AuthorSerializer(data=request.data)
        if author.is_valid():
            author.save()
        return Response(author.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
    """
    Retrieve, update or delete a code author.
    """
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        response = {"message": "author not exists"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        response = {"message": "bạn đã xóa thành công author id = " + str(pk)}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
