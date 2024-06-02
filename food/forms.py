from django import forms

class Accounts(forms.Form):
    name = forms.CharField(max_length=230)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    rpassword = forms.CharField(max_length=100)