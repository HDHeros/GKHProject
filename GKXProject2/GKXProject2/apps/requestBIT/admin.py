from django.contrib import admin

from .models import BIT_request_category, Status, BIT_request

admin.site.register(BIT_request_category)
admin.site.register(Status)
admin.site.register(BIT_request)
