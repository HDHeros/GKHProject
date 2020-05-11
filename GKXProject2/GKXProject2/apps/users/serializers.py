from rest_framework import serializers
from users.models import Profile, Mobile_Phone, Post, Work_Phone, Branch, Kab, Role
from fixed_assets.models import PC, Printer, Monitor, Fixed_assets, Type_catridge
from fixed_assets.serializers import PCSerializers, MonitorSerializers, PrinterSerializers
from django.contrib.auth.models import User

class Mobile_PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Phone
        fields = ("id","numder_mobile_phone") 

class Work_PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Work_Phone
        fields = ("id","number_work_phone")

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","name_post")

class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("id","name_branch")

class KabSerialializers(serializers.ModelSerializer):
    branch = BranchSerializers()
    work_phone = Work_PhoneSerializers()
    class Meta:
        model = Kab
        fields = ("id", "number_kab", "branch", "work_phone")

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name_role")

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    mobile_phone = Mobile_PhoneSerializers()
    post = PostSerializers()
    work_phone = Work_PhoneSerializers()
    kab = KabSerialializers()
    name_role = RoleSerializers()
    pc = PCSerializers()
    monitor = MonitorSerializers()
    printer = PrinterSerializers()
    class Meta:
        model = Profile
        fields = ("user", "flag_delete", "birth", "mobile_phone", "work_phone", "post", "kab", "name_role", "pc", "monitor", "printer")



