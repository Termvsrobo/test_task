# from django.core.exceptions import RegexValidator, FileExtensionValidator
from django.core.validators import FileExtensionValidator, RegexValidator

number_validator = RegexValidator(
    regex=r'\d{2}-\d{6}',
    message='Номер заявки не соответствует формату 00-000000'
)

order_file_extension_validator = FileExtensionValidator(allowed_extensions=['xlsx'])
