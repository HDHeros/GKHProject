# Generated by Django 3.0.4 on 2020-05-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixed_assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_assets', models.CharField(max_length=50, verbose_name='Наименование')),
                ('inv_number', models.CharField(max_length=10, verbose_name='Инвентарынй номер')),
            ],
            options={
                'verbose_name': 'Основное средство',
                'verbose_name_plural': 'Основыные средства',
            },
        ),
        migrations.CreateModel(
            name='Type_catridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_catridge', models.CharField(max_length=20, verbose_name='Наименование катриджа')),
            ],
            options={
                'verbose_name': 'Тип катриджа',
                'verbose_name_plural': 'Типы катриджей',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_printer', models.CharField(max_length=20, verbose_name='Наименование принтера')),
                ('inv_number', models.CharField(max_length=10, verbose_name='Инвентарынй номер')),
                ('fixed_assets', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fixed_assets.Fixed_assets', verbose_name='Принтер')),
                ('type_catridge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fixed_assets.Type_catridge', verbose_name='Тип катриджа')),
            ],
            options={
                'verbose_name': 'Принтер',
                'verbose_name_plural': 'Принтеры',
            },
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pc', models.CharField(max_length=50, verbose_name='Имя ПК')),
                ('ip_address', models.CharField(max_length=10, verbose_name='Ip адрес')),
                ('os', models.CharField(max_length=10, verbose_name='Операционная система')),
                ('inv_number', models.CharField(max_length=10, verbose_name='Инвентарынй номер')),
                ('fixed_assets', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fixed_assets.Fixed_assets', verbose_name='Инвентарный № ПК:')),
            ],
            options={
                'verbose_name': 'ПК',
                'verbose_name_plural': 'ПК',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_monitor', models.CharField(max_length=50, verbose_name='Наименование монитора')),
                ('inv_number', models.CharField(max_length=10, verbose_name='Инвентарынй номер')),
                ('fixed_assets', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fixed_assets.Fixed_assets', verbose_name='Инвентарный № монитора')),
            ],
            options={
                'verbose_name': 'Монитор',
                'verbose_name_plural': 'Мониторы',
            },
        ),
    ]
