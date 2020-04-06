from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from requestBIT.models import BIT_request
from requestBIT.serializers import BIT_requestSerializers

class BIT_requests(APIView):
    def get(self, request):
        request = BIT_request.objects.all()
        serializer = BIT_requestSerializers(request, many = True)
        return Response({"data": serializer.data})
