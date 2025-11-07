from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DesignRequest

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Краткое название заявки'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Опишите помещение, пожелания, площадь...'}),
        }
