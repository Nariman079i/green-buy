from django.forms import *
from .models import User, Order, Sale


class MainEnter(ModelForm):
    model = User

    class Meta:
        fields = '__all__'


class Orders(ModelForm):
    model = Order

    class Meta:
        fields = '__all__'


class Sales(ModelForm):
    model = Sale

    class Meta:
        fields = '__all__'
