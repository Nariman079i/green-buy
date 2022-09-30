from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


# Create your views here.
def index(requests):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(requests, 'main/index.html', context=context)


class RegUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/registration_page.html'
    success_url = reverse_lazy('registration_page')


class LogUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def registration_page(requests):
    file = 'main/registration_page.html'

    if requests.method == 'POST':
        form = MainEnter(requests.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = MainEnter()

    context = {
        'form': form
    }

    return render(requests, file, context=context)
