from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Your mail', max_length=100)
    password = forms.CharField(label='Your pass', max_length=100)
