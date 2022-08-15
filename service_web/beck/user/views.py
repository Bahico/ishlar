from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from user.models import User
from user.serializers import UserSerializer


@api_view(['GET'])
def users(request):
    com = User.objects.all()
    if com:
        serializer = UserSerializer(com, many=True)
        return Response(serializer.data)
    else:
        return Response("Not comment!")


class UserInformation(APIView):
    @staticmethod
    def get(request):
        print(request.user)
        if request.user.is_authenticated:
            print(request.user.username)
        return Response({"msg": "True"}, status=status.HTTP_200_OK)
