from django.db import models
from users.models import User

class BIT_request_category(models.Model):
    name_category = models.CharField('Наименование категории', max_length = 10)
    note = models.CharField('Примечание', max_length = 200)
    parent = models.ForeignKey('self', verbose_name='Родительская категория', blank=True,   null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_category

class Status(models.Model):
    name_status = models.CharField('Статус',max_length = 20)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name_status

class BIT_request(models.Model):
    name_user = models.ForeignKey(User, related_name = 'name_user', on_delete = models.PROTECT, verbose_name='Клиент')
    date_start = models.DateField('Дата создания заявки', auto_now = True)
    description = models.CharField('Описание', max_length = 200)
    status = models.ForeignKey(Status, on_delete = models.PROTECT, verbose_name='Статус')
    BIT_request_category = models.ForeignKey(BIT_request_category,on_delete = models.PROTECT, verbose_name='Тип заявки')
    user_executor = models.ForeignKey(User, related_name = 'user_executor', on_delete = models.PROTECT, verbose_name='Ответственный сотрудник BIT:')
    date_close = models.DateTimeField('Дата закрытия заявки',auto_now = True)
    
    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return 'Оставил(а) заявку: '+ str(self.name_user) + ' Дата: ' + str(self.date_start) 
    
   