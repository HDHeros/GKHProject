from rest_framework import serializers
from users.models import User, Mobile_Phone,Post

class Mobile_PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Phone
        fields = ("id","numder_mobile_phone") 

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","name_post")

class UserSerializers(serializers.ModelSerializer):

    mobile_phone = Mobile_PhoneSerializers()
    post = PostSerializers()
    class Meta:
        model = User
        fields = ("flag_delete","surname","name","middle_name","birth","login","password","mobile_phone","work_phone","post","kab","name_role","pc","monitor","printer")

