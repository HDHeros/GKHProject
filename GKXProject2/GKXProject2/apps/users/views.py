from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from users.models import Profile
from users.serializers import ProfileSerializers

class Users(APIView):
    #permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        users = Profile.objects.all()
        serializer = ProfileSerializers(users, many = True)
        return Response({"data": serializer.data})
