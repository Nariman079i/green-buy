
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='home'),
    path('registration_page', RegUser.as_view()),
    path('login', LogUser.as_view())

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
