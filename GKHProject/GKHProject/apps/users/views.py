from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from users.models import User
from users.serializers import UserSerializers

class Users(APIView):
    #permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many = True)
        return Response({"data": serializer.data})

