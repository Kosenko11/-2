from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import DesignRequest

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



class DesignRequestForm(forms.ModelForm):
    class Meta:
        CATEGORY_CHOICES = [
            ('1', 'Категория 1'),
            ('2', 'Категория 4'),
            ('3', 'Категория 3'),
        ]
        model = DesignRequest
        fields = ['title', 'description', 'category', 'image']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Краткое название заявки'}),
            'Description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Опишите помещение, пожелания, площадь...'}),
            'Category': forms.ChoiceField(choices=CATEGORY_CHOICES, label='Выберите категорию')

        }

