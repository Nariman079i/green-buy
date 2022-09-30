from django.contrib.auth.forms import UserCreationForm , User
from django.forms import *
from .models import Order, Sale


class MainEnter(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'type': 'text', 'placeholder': 'Фамилия'
            }),
            'password1': TextInput(attrs={
                'type': 'text', 'placeholder': 'Имя'
            }),
            'password2': TextInput(attrs={
                'type': 'tel', 'placeholder': 'Номер телефона'
            }),
        }


class Orders(ModelForm):
    model = Order

    class Meta:
        fields = '__all__'


class Sales(ModelForm):
    model = Sale

    class Meta:
        fields = '__all__'
