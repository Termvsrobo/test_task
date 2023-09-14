import datetime

from django.http import HttpResponse
from django.views.generic.edit import FormView

from orders.forms import IndexForm, ReportForm
from orders.utils import get_report_data, get_wb, load_orders_from_excel


class IndexFormView(FormView):
    template_name = "index.html"
    form_class = IndexForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        excel_file = request.FILES["file"]
        load_orders_from_excel(excel_file)
        return super().post(request, *args, **kwargs)


class ReportView(FormView):
    template_name = "report.html"
    form_class = ReportForm

    def post(self, request, *args, **kwargs):
        from_date = datetime.datetime.strptime(
            request.POST['from_date'], '%d.%m.%Y %H:%M:%S'
        ) if request.POST['from_date'] else None
        to_date = datetime.datetime.strptime(
            request.POST['to_date'], '%d.%m.%Y %H:%M:%S'
        ) if request.POST['to_date'] else None
        result = get_report_data(from_date, to_date)
        wb = get_wb(result)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="result.xlsx"'
        wb.save(response)
        return response
