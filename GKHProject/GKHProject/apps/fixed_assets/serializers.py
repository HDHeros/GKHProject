from rest_framework import serializers
from fixed_assets.models import PC, Printer, Monitor, Fixed_assets, Type_catridge

class Fixed_assetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fixed_assets
        fields = ("id", "name_assets", "inv_number")

class MonitorSerializers(serializers.ModelSerializer):
    fixed_assets = Fixed_assetsSerializers()
    class Meta:
        model = Monitor
        fields = ("id", "fixed_assets", "name_monitor", "inv_number")

class PCSerializers(serializers.ModelSerializer):
    fixed_assets = Fixed_assetsSerializers()
    class Meta:
        model = PC
        fields = ("id", "fixed_assets","name_pc", "ip_address", "os", "inv_number")
       

class Type_catridgeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type_catridge
        fields = ("id","name_catridge")  

class PrinterSerializers(serializers.ModelSerializer):
    fixed_assets = Fixed_assetsSerializers()
    type_catridge = Type_catridgeSerializers()
    class Meta:
        model = Printer
        fields = ("id", "fixed_assets", "type_catridge", "name_printer", "inv_number")
