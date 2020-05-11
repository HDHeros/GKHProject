from rest_framework import serializers
from requestBIT.models import BIT_request, Status, BIT_request_category
from users.serializers import UserSerializers
class BIT_request_categorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BIT_request_category
        fields = ("id", "name_category", "note","parent")

class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "name_status")


class BIT_requestSerializers(serializers.ModelSerializer):
    name_user = UserSerializers()
    status = StatusSerializers()
    BIT_request_category = BIT_request_categorySerializers()
    user_executor = UserSerializers()
    class Meta:
        model = BIT_request
        fields = ("id", "name_user", "date_start", "description","status","BIT_request_category","user_executor","date_close")