from django import forms

class buyForm(forms.Form):
    stock = forms.CharField(label="stockOption", max_length=6)
    shares = forms.IntegerField(label="numberShares", max_value=10)

class sellForm(forms.Form):
    stock = forms.CharField(label="stockOption", max_length=6)
    shares = forms.IntegerField(label="numberShares", max_value=10)