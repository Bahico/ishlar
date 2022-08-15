import rest_framework.request
from django.http import FileResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service.models import Task, Like, DisLike
from service.serializers import TaskSerializer, DisLikeSerializer, LikeSerializer


@api_view(['GET'])
def taskList(request: rest_framework.request.Request, pk):
    tasks = Task.objects.all().order_by('id')[:int(pk)]
    if tasks:
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)  # , status=status.HTTP_200_OK)
    else:
        return Response([])





@api_view(['GET'])
def taskDetail(request: rest_framework.request.Request, pk):
    task = Task.objects.filter(id=pk)
    if task:
        author = 'false'
        if task[0].author == request.user.id:
            author = 'true'
        serializer = TaskSerializer(task, many=False)
        return Response({'post': serializer.data, 'type': author})
    else:
        return Response("Not post!")


@api_view(['POST'])
def taskCreate(request: rest_framework.request.Request):
    data = request.data
    data['author'] = request.user.id
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request: rest_framework.request.Request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def taskDelete(request: rest_framework.request.Request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully delete!")


@api_view(['GET'])
def taskViews(request: rest_framework.request.Request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.views += 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")


@api_view(['POST'])
def taskLike(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        task = Task.objects.get(id=request.data['post_id'])
        like = Like.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if like:
            return Response('Not item!')
        else:
            serializer = LikeSerializer(data={'post_id': request.data['post_id'], 'author': user[0].user_id})
            if serializer.is_valid():
                serializer.save()
                task.like += 1
                task.save()
                return Response("Success full!")
            else:
                print(serializer.errors)
                return Response('Not item!')
    else:
        return Response('Error!')


@api_view(['POST'])
def taskLike_(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        task = Task.objects.get(id=request.data["post_id"])
        like = Like.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if like:
            like.delete()
            task.like -= 1
            task.save()
            return Response("Success full!")
        else:
            return Response('Not item!')
    else:
        return Response('Error!')


@api_view(['POST'])
def taskDisLike(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        task = Task.objects.get(id=request.data["post_id"])
        dislike = DisLike.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if dislike:
            return Response("Error!")
        else:
            serializer = DisLikeSerializer(data={'post_id': request.data['post_id'], 'author': user[0].user_id})
            if serializer.is_valid():
                serializer.save()
                task.dislike += 1
                task.save()
                return Response("Success full!")
            else:
                return Response("Error!")
    else:
        return Response("Error!")


@api_view(['POST'])
def taskDisLike_(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        task = Task.objects.get(id=request.data["post_id"])
        dislike = DisLike.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if dislike:
            dislike.delete()
            task.dislike -= 1
            task.save()
            return Response("Success full!")
        else:
            return Response("Not item!")
    else:
        return Response("Error!")


@api_view(['POST'])
def taskLikeView(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        like = Like.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if like:
            return Response("True")
        else:
            return Response("False")
    else:
        return Response("Error!")


@api_view(['POST'])
def taskDisLikeView(request: rest_framework.request.Request):
    user = Token.objects.filter(key=request.data['author'])
    if user:
        dislike = DisLike.objects.filter(post_id=request.data["post_id"], author=user[0].user_id)
        if dislike:
            return Response("True")
        else:
            return Response("False")
    else:
        return Response("Error!")


@api_view(['GET'])
def taskAuthorService(request: rest_framework.request.Request):
    services = Task.objects.filter(author=request.user.id)
    if services:
        serializer = TaskSerializer(services, many=True)
        return Response(serializer.data)
    else:
        return Response("Not service!")
