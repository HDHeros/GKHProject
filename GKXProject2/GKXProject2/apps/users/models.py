from django.db import models
from fixed_assets.models import PC, Printer, Monitor
from django.contrib.auth.models import User

class Mobile_Phone(models.Model):
    numder_mobile_phone = models.CharField('Номер моб. телуфона', max_length= 13, unique = True)

    class Meta:
        verbose_name = 'Номер мобильного телефона'
        verbose_name_plural = 'Номера мобильных телефонов'

    def __str__(self):
        return self.numder_mobile_phone

class Post(models.Model):
    name_post = models.CharField('Должность', max_length= 20)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name_post

class Branch(models.Model):
    name_branch = models.CharField('Отдел', max_length = 20)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
    
    def __str__(self):
        return self.name_branch

class Work_Phone(models.Model):
    number_work_phone = models.CharField('Городской телефон', max_length = 10, unique = True)

    class Meta:
        verbose_name = 'Номер городского телефона'
        verbose_name_plural = 'Номера городских телефонов'

    def __str__(self):
        return self.number_work_phone
    
class Kab(models.Model):
    number_kab = models.CharField('Номер кабинета', max_length = 5)
    branch = models.ForeignKey(Branch, on_delete = models.PROTECT, verbose_name = 'Отдел')
    work_phone = models.ForeignKey(Work_Phone, on_delete = models.PROTECT, verbose_name = 'Городской телефон')

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return self.number_kab

class Role(models.Model):
    name_role = models.CharField('Роль', max_length = 20)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
    
    def __str__(self):
        return self.name_role

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    flag_delete = models.BooleanField(default = False)
    birth = models.DateField('Дата рождения')
    mobile_phone = models.ForeignKey(Mobile_Phone, on_delete = models.CASCADE, verbose_name='Мобильный телефон')
    work_phone = models.ForeignKey(Work_Phone, on_delete = models.PROTECT, verbose_name='Городской телефон')
    post = models.ForeignKey(Post, on_delete = models.PROTECT, verbose_name='Должность')
    kab = models.ForeignKey(Kab, on_delete = models.PROTECT, verbose_name='Кабинет')
    name_role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name='Роль')
    pc = models.OneToOneField(PC, on_delete = models.PROTECT, verbose_name='ПК')
    monitor = models.OneToOneField(Monitor, on_delete = models.PROTECT, verbose_name='Монитор')
    printer = models.OneToOneField(Printer, on_delete = models.PROTECT, verbose_name='Принтер')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
