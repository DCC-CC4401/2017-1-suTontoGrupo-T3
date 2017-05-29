from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your pass', max_length=100)

class EditVForm(forms.Form):
    name= forms.CharField(label= 'Your name', max_length=100)
    #file= forms.FileField()

class SignupForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100)
    usertype = forms.CharField(label='Usertype', max_length=1)
    email = forms.CharField(label='Your email', max_length=100)
    hora_inicio  = forms.TimeField(label='Initial time')
    hora_final = forms.TimeField(label='Final time')
    efectivo  = forms.BooleanField(label='Cash')
    tarjeta_credito = forms.BooleanField(label='Credit Card')
    tarjeta_debito = forms.BooleanField(label='Debit Card')
    tarjeta_junaeb = forms.BooleanField(label='Junaeb Card')