from django.db.models import *


# Create your models here.
class User(Model):
    last_name = CharField('Фамилия', max_length=30, null=False)
    first_name = CharField('Имя', max_length=30, null=False)
    tell = CharField('Номер телефона', max_length=11, null=False)
    date_registration = DateField('Дата регистрации', auto_now_add=True)


class Product(Model):
    title = CharField('Наименование продукта', max_length=30)
    img = ImageField('Изображение продукта', upload_to='img/')
    price = IntegerField('Цена продукта')
    unit_id = ForeignKey('Unit', on_delete=PROTECT)
    cat_id = ForeignKey('Categories', on_delete=CASCADE)


class Categories(Model):
    title = CharField('Наименование категории', max_length=50)
    slug = SlugField('Ссылка', max_length=30)


class City(Model):
    title = CharField('Наименование города', max_length=100)


class Street(Model):
    city_id = ForeignKey(City, on_delete=CASCADE)
    title = CharField('Наименование улицы')


class Unit(Model):
    title = CharField('Единица измерения', max_length=10)


class Order(Model):
    user_id = ForeignKey('User', on_delete=CASCADE)
    product_id = ForeignKey('Product', on_delete=CASCADE)
    count = IntegerField()

class Sale(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    product_id = ForeignKey(Product, on_delete=CASCADE)
    street_id = ForeignKey(Street , on_delete=CASCADE)
