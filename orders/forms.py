from django import forms


class IndexForm(forms.Form):
    file = forms.FileField()


class ReportForm(forms.Form):
    from_date = forms.DateTimeField(widget=forms.DateTimeInput())
    to_date = forms.DateTimeField(widget=forms.DateTimeInput())
