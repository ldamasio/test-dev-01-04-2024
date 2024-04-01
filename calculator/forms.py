from django import forms

class CalcForm(forms.Form):
    month1 = forms.IntegerField(max_length = 20)
    month2 = forms.IntegerField(max_length = 20)
    month3 = forms.IntegerField(max_length = 20)
    tax = forms.DecimalField(max_length = 200)
    tax_type = forms.CharField(max_length=220)
