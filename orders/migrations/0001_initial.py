# Generated by Django 4.2.5 on 2023-09-12 08:01

import django.core.validators
from django.db import migrations, models
import django_enum.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания заявки')),
                ('number', models.CharField(validators=[django.core.validators.RegexValidator(message='Номер заявки не соответствует формату 00-000000', regex='\\d{2}-\\d{6}')], verbose_name='Номер заявки')),
                ('state', models.CharField(verbose_name='Состояние заявки')),
                ('agreement', django_enum.fields.EnumCharField(choices=[('A1', 'Материал не выбран'), ('A2', 'Расширен без согласования'), ('A3', 'Расширен после согласования'), ('A4', 'Согласование не требуется')], max_length=2, verbose_name='Согласование')),
                ('status', django_enum.fields.EnumCharField(choices=[('S1', 'В обработке (повторно)'), ('S2', 'В обработке (подтверждена)'), ('S3', 'Возвращена на уточнение'), ('S4', 'Обработка завершена'), ('S5', 'Отправлена в обработку'), ('S6', 'Отправлена в обработку (повторно)')], max_length=2, verbose_name='Статус заявки')),
                ('author', models.CharField(verbose_name='Автор заявки')),
                ('filename', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx'])], verbose_name='Имя файла')),
                ('end_of_work_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания обработки')),
                ('duration', models.CharField(verbose_name='Время от создания заявки до конца обработки (в часах)')),
                ('fullname', models.CharField(verbose_name='Полное наименование изначальное')),
                ('fullname_after_proccess', models.CharField(blank=True, null=True, verbose_name='Полное наименование после обработки')),
                ('materials_code', models.CharField(blank=True, null=True, verbose_name='Код материала')),
                ('same_materials', models.CharField(verbose_name='Похожие материалы полученные из КП')),
                ('bei', models.CharField(blank=True, null=True, verbose_name='БЕИ')),
                ('ntd', models.CharField(blank=True, null=True, verbose_name='НТД')),
                ('package_id', models.CharField()),
            ],
        ),
    ]