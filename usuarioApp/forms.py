from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES = [
        ('Docente', 'Docente'),
        ('Discente', 'Discente'),
        ('Técnico Administrativo em Educação', 'Técnico Administrativo em Educação')
    ]

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name',]

    username = forms.CharField(label='Matrícula:')
    email = forms.EmailField(label='Email:')
    last_name = forms.CharField(label='Nome Completo:')
    first_name = forms.ChoiceField(
        label='Status:',
        choices=FIRST_NAME_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='Discente'
    )





