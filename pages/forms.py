from django import forms

class stockActions(forms.Form):
    stock = forms.CharField(label="stockOption", max_length=10)
    shares = forms.IntegerField(label="numberShares", max_value=10000)