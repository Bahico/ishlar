
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from comment.models import Comment
from comment.serializers import CommentSerializer


# Create your views here.


@api_view(['GET'])
def comments(request):
    com = Comment.objects.all()
    if com:
        serializer = CommentSerializer(com, many=True)
        return Response(serializer.data)
    else:
        return Response("Not comment!")


@api_view(['POST'])
def commentCreate(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['GET'])
def comment(request, id, pk):
    com = Comment.objects.filter(post_id=id).order_by('post_id')[:int(pk)]
    if com:
        serializer = CommentSerializer(com, many=True)
        return Response(serializer.data)
    else:
        return Response("Not comment!")


@api_view(['GET'])
def commentDelete(request, id):
    com = Comment.objects.get(id=id)
    com.delete()
    return Response("Item successfully delete!")


@api_view(['GET'])
def commentPhoto(request, id):
    com = Comment.objects.get(id=id).photo
    if com:
        img = open(f'img/{com}', 'rb')
        return FileResponse(img)
    else:
        return Response("Not comment!")
