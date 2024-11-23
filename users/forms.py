from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário',widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)

class SignupForms(forms.Form):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)
    password_confirm = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, max_length=20)


    def clean_username(self):
        username = self.cleaned_data['username']
        
        if username:
            username = username.lower().strip()

            if " " in username:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
        
        return username
    
    def clean_password_confirm(self):
        senha_1 = self.cleaned_data.get('password')
        senha_2 = self.cleaned_data.get('password_confirm')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2