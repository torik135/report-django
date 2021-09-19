from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name', 'remarks')
        widgets = {
            'remarks': forms.Textarea(attrs={
                'class': 'materialize-textarea',
                'id': 'textarea-remarks',
            })
        }