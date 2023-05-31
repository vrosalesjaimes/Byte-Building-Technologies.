from django import forms


class FormAdmin(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
