from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário',widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)

class SignupForms(forms.Form):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)
    password_confirm = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)