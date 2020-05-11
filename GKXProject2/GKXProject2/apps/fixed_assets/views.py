from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from fixed_assets.models import PC
from fixed_assets.serializers import PCSerializers

class PC_C(APIView):
    def get(self, request):
        pc = PC.objects.all()
        serializer = PCSerializers(pc, many = True)
        return Response({"data": serializer.data})