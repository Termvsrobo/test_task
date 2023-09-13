from enum import Enum

from django.db import models
from django_enum import EnumField

from orders.validators import number_validator, order_file_extension_validator

# Create your models here.


class Order(models.Model):

    class AgreementEnum(str, Enum):
        NOT_SELECTED = 'Материал не выбран'
        EXTENDED_WITHOUT_AGREEMENT = 'Расширен без согласования'
        EXTENDED_AFTER_AGREEMENT = 'Расширен после согласования'
        AGREEMENT_NOT_REQUIRED = 'Согласование не требуется'

    class StatusEnum(str, Enum):
        IN_PROCESS_AGAIN = 'В обработке (повторно)'
        IN_PROCESS_ACCEPTED = 'В обработке (подтверждена)'
        RETURNED_FOR_CLARIFICATION = 'Возвращена на уточнение'
        PROCESSED = 'Обработка завершена'
        RETURNED_FOR_PROCESS = 'Отправлена в обработку'
        RETURNED_FOR_PROCESS_AGAIN = 'Отправлена в обработку (повторно)'

    number = models.CharField(validators=[number_validator], verbose_name='Номер заявки')
    state = models.CharField(verbose_name='Состояние заявки')
    agreement = EnumField(AgreementEnum, verbose_name='Согласование')
    status = EnumField(StatusEnum, verbose_name='Статус заявки')
    author = models.CharField(verbose_name='Автор заявки')
    filename = models.FileField(validators=[order_file_extension_validator], verbose_name='Имя файла')
    created_at = models.DateTimeField(verbose_name='Дата создания заявки')
    end_of_work_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания обработки')
    duration = models.CharField(verbose_name='Время от создания заявки до конца обработки (в часах)')
    fullname = models.CharField(verbose_name='Полное наименование изначальное')
    fullname_after_proccess = models.CharField(
        null=True, blank=True, verbose_name='Полное наименование после обработки'
    )
    materials_code = models.CharField(null=True, blank=True, verbose_name='Код материала')
    same_materials = models.CharField(null=True, blank=True, verbose_name='Похожие материалы полученные из КП')
    bei = models.CharField(null=True, blank=True, verbose_name='БЕИ')
    ntd = models.CharField(null=True, blank=True, verbose_name='НТД')
    package_id = models.CharField(verbose_name='ID пакета')
