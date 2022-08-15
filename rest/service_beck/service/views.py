import rest_framework.request
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service.models import Task
from service.serializers import TaskSerializer


@api_view(['GET'])
def taskList(request, pk):
    tasks = Task.objects.all().order_by('id')[:int(pk)]
    if tasks:
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)  # , status=status.HTTP_200_OK)
    else:
        return Response([])


@api_view(['GET'])
def taskPhoto(request, pk):
    task = Task.objects.get(id=pk).photo
    img = open('img/' + str(task), 'rb')
    return FileResponse(img)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    else:
        return Response("Not post!")


@api_view(['POST'])
def taskCreate(request: rest_framework.request.Request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully delete!")


@api_view(['GET'])
def taskViews(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.views += 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")


@api_view(['GET'])
def taskLike(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.like += 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")


@api_view(['GET'])
def taskLike_(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.like -= 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")


@api_view(['GET'])
def taskDisLike(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.dislike += 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")


@api_view(['GET'])
def taskDisLike_(request, pk):
    task = Task.objects.get(id=pk)
    if task:
        task.dislike -= 1
        task.save()
        return Response("Success full!")
    else:
        return Response("Not item!")
