from django import forms
from shop2.models import FormModel


class FormModelForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['username', 'age', 'comment']
