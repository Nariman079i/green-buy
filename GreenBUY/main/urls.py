
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
] + static(settings.MEDIA_ROOT,document_root=settings.MEDIA_ROOT)