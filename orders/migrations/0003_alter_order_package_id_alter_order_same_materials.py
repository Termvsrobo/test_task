# Generated by Django 4.2.5 on 2023-09-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_agreement_alter_order_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='package_id',
            field=models.CharField(verbose_name='ID пакета'),
        ),
        migrations.AlterField(
            model_name='order',
            name='same_materials',
            field=models.CharField(blank=True, null=True, verbose_name='Похожие материалы полученные из КП'),
        ),
    ]
