from django.db import models
from fixed_assets.models import PC, Printer, Monitor

class Mobile_Phone(models.Model):
    numder_mobile_phone = models.CharField('Номер моб. телуфона', max_length= 13)

class Post(models.Model):
    name_post = models.CharField('Должность', max_length= 20)

class Branch(models.Model):
    name_branch = models.CharField('Отдел', max_length = 20)

class Work_Phone(models.Model):
    number_work_phone = models.CharField('Городской телефон', max_length = 10)

class Kab(models.Model):
    number_kab = models.CharField('Номер кабинета', max_length = 5)
    branch = models.ForeignKey(Branch, on_delete = models.PROTECT)
    work_phone = models.ForeignKey(Work_Phone, on_delete = models.PROTECT)

class Role(models.Model):
    name_role = models.CharField('Роль', max_length = 20)

class User(models.Model):
    flag_delete = models.BooleanField(default = False)
    surname = models.CharField('Фамилия', max_length = 20)
    name = models.CharField('Имя', max_length = 20)
    middle_name = models.CharField('Отчество', max_length= 20)
    birth = models.DateTimeField('Дата рождения')
    login = models.CharField('Логин', max_length= 20)
    password = models.CharField('Пароль',max_length= 20)
    mobile_phone = models.ForeignKey(Mobile_Phone, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.PROTECT)
    kab = models.ForeignKey(Kab, on_delete = models.PROTECT)
    work_phone = models.ForeignKey(Work_Phone, on_delete = models.PROTECT)
    name_role = models.ForeignKey(Role, on_delete = models.PROTECT)
    pc = models.OneToOneField(PC, on_delete = models.PROTECT)
    printer = models.OneToOneField(Printer, on_delete = models.PROTECT)
    monitor = models.OneToOneField(Monitor, on_delete = models.PROTECT)
