from django.contrib import admin

from .models import Fixed_assets, Monitor, PC, Type_catridge, Printer

admin.site.register(Fixed_assets)
admin.site.register(Monitor)
admin.site.register(PC)
admin.site.register(Type_catridge)
admin.site.register(Printer)
