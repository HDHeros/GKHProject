from django.db import models
from users.models import User

class BIT_request_category(models.Model):
    name_category = models.CharField('Наименование категории', max_length = 10)
    note = models.CharField('Примечание', max_length = 200)
    parent = models.ForeignKey('self', verbose_name='Родительская категория', blank=True,   null=True, on_delete=models.CASCADE)

class Status(models.Model):
    name_status = models.CharField('Статус',max_length = 20)

class BIT_request(models.Model):
    name_user = models.ForeignKey(User, related_name = 'name_user', on_delete = models.PROTECT)
    date_start = models.DateTimeField('Дата создания заявки',auto_now = True)
    description = models.CharField('Описание', max_length = 200)
    status = models.ForeignKey(Status, on_delete = models.PROTECT)
    BIT_request_category = models.ForeignKey(BIT_request_category,on_delete = models.PROTECT)
    user_executor = models.ForeignKey(User, related_name = 'user_executor', on_delete = models.PROTECT)
    date_close = models.DateTimeField('Дата закрытия заявки',auto_now = True)