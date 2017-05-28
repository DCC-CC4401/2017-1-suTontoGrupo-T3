from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your pass', max_length=100)

class EditVForm(forms.Form):
    your_name= forms.CharField(label= 'Your name', max_length=100)
    file= forms.FileField()
