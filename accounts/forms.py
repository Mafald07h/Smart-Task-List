from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Nome de usuário"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Digite a sua senha"
            }
        )
    )

class CadastroForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Username"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email"
            }
        )
    )
    senha1 = forms.CharField(
        label="Password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Password"
            }
        )
    )
    senha2 = forms.CharField(
        label="Confirm password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Confirm password"
            }
        )
    )