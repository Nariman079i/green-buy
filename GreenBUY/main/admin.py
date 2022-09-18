from django.contrib import admin
from .models import *

models_db = [User, Unit, City, Categories, Product, Street, Sale, Order]

for db in models_db:
    admin.site.register(db)
