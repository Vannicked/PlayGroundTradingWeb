from django import forms

class buyForm(forms.Form):
    stock = forms.CharField(label="stockOption", max_length=10)
    shares = forms.IntegerField(label="numberShares", max_value=10000)

class sellForm(forms.Form):
    stock = forms.CharField(label="stockOption", max_length=10)
    shares = forms.IntegerField(label="numberShares", max_value=10000)