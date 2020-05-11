from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users import models
from .models import Mobile_Phone, Post, Branch, Work_Phone, Kab, Role, Profile

admin.site.register(Mobile_Phone)
admin.site.register(Post)
admin.site.register(Branch)
admin.site.register(Work_Phone)
admin.site.register(Kab)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

