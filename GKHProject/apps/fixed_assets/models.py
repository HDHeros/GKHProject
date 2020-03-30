from django.db import models

class Fixed_assets(models.Model):
    name_assets = models.CharField('Наименование', max_length = 50)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)

class Monitor(models.Model):
    name_monitor = models.CharField('Наименование монитора', max_length = 50)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT) 

class PC(models.Model):
    name_pc = models.CharField('Наименование ПК', max_length = 50)
    ip_address = models.CharField('Ip адрес', max_length = 10)
    os = models.CharField('Операционная система', max_length = 10)
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT) 

class Type_catridge(models.Model):
    name_catridge = models.CharField('Наименование катриджа',max_length = 20)

class Printer(models.Model):
    name_printer = models.CharField('Наименование принтера', max_length = 20)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT)
    type_catridge = models.ForeignKey(Type_catridge, on_delete = models.PROTECT)
