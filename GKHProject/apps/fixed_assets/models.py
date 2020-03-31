from django.db import models

class Fixed_assets(models.Model):
    name_assets = models.CharField('Наименование', max_length = 50)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)

    class Meta:
        verbose_name = 'Основное средство'
        verbose_name_plural = 'Основыные средства'
    
    def __str__(self):
        return self.name_assets + ' Инв. №'+ self.inv_number

class Monitor(models.Model):
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT, verbose_name='Инвентарный № монитора') 
    name_monitor = models.CharField('Наименование монитора', max_length = 50)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)
    
    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'

    def __str__(self):
        return str(self.fixed_assets)

class PC(models.Model):
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT, verbose_name='Инвентарный № ПК:') 
    name_pc = models.CharField('Имя ПК', max_length = 50)
    ip_address = models.CharField('Ip адрес', max_length = 10)
    os = models.CharField('Операционная система', max_length = 10)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)
    
    class Meta:
        verbose_name = 'ПК'
        verbose_name_plural = 'ПК'
    
    def __str__(self):
        return str(self.fixed_assets)
    
class Type_catridge(models.Model):
    name_catridge = models.CharField('Наименование катриджа',max_length = 20)

    class Meta:
        verbose_name = 'Тип катриджа'
        verbose_name_plural = 'Типы катриджей'

    def __str__(self):
        return self.name_catridge

class Printer(models.Model):
    fixed_assets = models.ForeignKey(Fixed_assets, on_delete = models.PROTECT, verbose_name='Принтер')
    type_catridge = models.ForeignKey(Type_catridge, on_delete = models.PROTECT, verbose_name='Тип катриджа')
    name_printer = models.CharField('Наименование принтера', max_length = 20)
    inv_number = models.CharField('Инвентарынй номер', max_length = 10)

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
    
    def __str__(self):
        return str(self.fixed_assets)