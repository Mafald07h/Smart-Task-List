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