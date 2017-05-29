from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your pass', max_length=100)

class EditVForm(forms.Form):
    name= forms.CharField(label= 'Your name', max_length=100)
    #file= forms.FileField()

class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    usertype = forms.MultipleChoiceField(choices = [('1', 'fijo'), ('2', 'ambulante'), ('3', 'alumno')])
    email = forms.CharField(label='email', max_length=100)
    hora_inicial  = forms.TimeField()
    hora_final = forms.TimeField()
    efectivo = forms.Field(label="efectivo")
    tarjeta_credito = forms.Field(label="tarjeta_credito")
    tarjeta_debito = forms.Field(label="tarjeta_debito")
    tarjeta_junaeb = forms.Field(label="tarjeta_junaeb")