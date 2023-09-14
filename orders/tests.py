import datetime
from pathlib import Path

from django.core.exceptions import ValidationError
from django.test import TestCase

from orders.models import Order
from orders.utils import get_report_data, get_wb, load_orders_from_excel


class OrdersTestCase(TestCase):
    def test_invalid_number(self):
        order = Order(number='asdfasdf')
        with self.assertRaises(ValidationError) as err:
            order.full_clean()
        exc = err.exception
        errors_msg = [error.message for error in exc.error_dict['number']]
        self.assertIn('Номер заявки не соответствует формату 00-000000', errors_msg)

    def test_invalid_agreement(self):
        order = Order(agreement='asdfasdf')
        with self.assertRaises(ValidationError) as err:
            order.full_clean()
        exc = err.exception
        errors_msg = [error.message for error in exc.error_dict['agreement']]
        self.assertIn("'asdfasdf' is not a valid AgreementEnum.", errors_msg)

    def test_invalid_status(self):
        order = Order(status='asdfasdf')
        with self.assertRaises(ValidationError) as err:
            order.full_clean()
        exc = err.exception
        errors_msg = [error.message for error in exc.error_dict['status']]
        self.assertIn("'asdfasdf' is not a valid StatusEnum.", errors_msg)

    def test_invalid_filename(self):
        order = Order(filename='asdfasdf.py')
        with self.assertRaises(ValidationError) as err:
            order.full_clean()
        exc = err.exception
        errors_msg = [error.message for error in exc.error_dict['filename']]
        self.assertIn(
            'File extension “%(extension)s” is not allowed. Allowed extensions are: %(allowed_extensions)s.',
            errors_msg
        )


class LoadExcelTestCase(TestCase):
    def test_load_excel(self):
        excel_filename = Path(__file__).parent / Path('data_for_tests') / Path('testing_data.xlsx')
        load_orders_from_excel(excel_filename)
        self.assertEqual(Order.objects.count(), 1016)


class ReportTestCase(TestCase):
    fixtures = (Path(__file__).parent / Path('fixtures') / Path('order.json'),)

    fake_result = [
        {'name_param': 'Загруженных заявок', 'count_period': 1, 'count_all': 1016},
        {'name_param': 'Дубли', 'count_period': 0, 'count_all': 355},
        {'name_param': 'На создание', 'count_period': 1, 'count_all': 577},
        {'name_param': 'На расширение', 'count_period': 0, 'count_all': 84},
        {'name_param': 'Обработка завершена', 'count_period': 0, 'count_all': 961},
        {'name_param': 'Возвращена на уточнение', 'count_period': 0, 'count_all': 8},
        {'name_param': 'Отправлена в обработку', 'count_period': 1, 'count_all': 43},
        {'name_param': 'Пакетов', 'count_period': 1, 'count_all': 123},
        {'name_param': 'Пользователей', 'count_period': 1, 'count_all': 21}
    ]

    def test_report(self):
        from_date = datetime.datetime(2023, 8, 22, 9, 43, 50)
        to_date = datetime.datetime(2023, 8, 22, 9, 43, 50)
        result = get_report_data(from_date, to_date)
        self.assertListEqual(
            result,
            self.fake_result
        )

    def test_wb(self):
        wb = get_wb(self.fake_result)
        result_data = [
            {'name_param': 'Название', 'count_period': 'За указанный период', 'count_all': 'За все время'}
        ] + self.fake_result

        _field_map = {
            'A': 'name_param',
            'B': 'count_period',
            'C': 'count_all',
        }

        ws = wb["Result"]
        for row, test_data in zip(ws.iter_rows(), result_data):
            for col in row:
                self.assertEqual(col.value, test_data[_field_map[col.column_letter]])
