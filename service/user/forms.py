from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Request

class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(label='ФИО', max_length=150)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)
    consent = forms.BooleanField(label='Согласие на обработку персональных данных')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Пароли не совпадают")
        return p2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким логином уже существует")
        return username

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"row": 4}),
        }
