from django.http import FileResponse
import rest_framework.request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User

from .serializer import UserSerializer


# Create your views here.


# @api_view(['GET'])
# def userList(request):
#     users = User.objects.all()
#     if users:
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response("Not user")


# @api_view(['POST'])
# def userRegistration(request):
#     user = User.objects.filter(phone_number=request.data['phone_number'])
#     if user:
#         return Response("Error!")
#     else:
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             print(serializer.errors)
#             return Response("Error!")


# @api_view(['POST'])
# def userLogin(request):
#     user = User.objects.filter(phone_number=request.data['phone_number'], password=request.data['password'])
#     if user:
#         return Response(dict(type='id', id=user[0].id))
#     else:
#         return Response(dict(type="error"))


# @api_view(['GET'])
# def userImage(request, id):
#     user = UserSerializer(id)
#     print(user)
#     if user:
#         image = open("img/" + str(user[0].image), 'rb')
#         return FileResponse(image)
#     else:
#         return Response("Not image!")


# @api_view(['GET'])
# def userImageUser(request: rest_framework.request.Request, id):
#     user = Token.objects.filter(key=id)
#     if user:
#         user = User.objects.filter(id=user[0].user_id)
#         if user[0].image:
#             image = open("img/" + str(user[0].image), 'rb')
#             return FileResponse(image)
#         else:
#             image = open("img/img_avatar.png", 'rb')
#             return FileResponse(image)
#     else:
#         image = open("img/img_avatar.png", 'rb')
#         return FileResponse(image)


@api_view(['GET'])
def userImageId(request: rest_framework.request.Request):
    user = User.objects.get(id=request.user.id)
    if user.image:
        image = open("img/" + str(user.image), 'rb')
        return FileResponse(image)
    else:
        image = open("img/img_avatar.png", 'rb')
        return FileResponse(image)


@api_view(['POST'])
def userImageEdit(request: rest_framework.request.Request, id):
    request.user.image = request.data['image']
    request.user.save()


@api_view(['GET'])
def userInformationView(request: rest_framework.request.Request):
    serializer = UserSerializer(request.user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request: rest_framework.request.Request):
    request.user.description = request.data['description']
    request.user.save()
    return Response('Good!')


@api_view(['GET'])
def userDelPhoto(request: rest_framework.request.Request):
    request.user.image.delete(save=True)
    return Response("Good")


@api_view(['GET'])
def userAuthor(request: rest_framework.request.Request):
    return Response(request.user.phone_number)


@api_view(['GET'])
def userIdView(request: rest_framework.request.Request):
    return Response(request.user.id)
