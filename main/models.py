from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Product(models.Model):
    ENGINE_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electro', 'Электро'),
        ('hybrid', 'Гибрид'),
        ('diesel gas', 'Дизель+газ'),
        ('petrol gas', 'Бензин+газ'),
        ('gas', 'Газ'),
        ('not specified', 'Не указано'),
    ]

    STEERING_WHEEL_CHOICES = [
        ('right', 'Правый'),
        ('left', 'Левый'),
    ]

    TRANSMISSION_CHOICES = [
        ('automatic', 'Автомат'),
        ('mechanical', 'Механическая'),
        ('pneumatic', 'Пневматическая'),
        ('robot', 'Робот'),
        ('variable', 'Вариатор'),
        ('not specified', 'Не указано'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    # discount = models.PositiveIntegerField(verbose_name='Скидка, %', default=0)
    year_of_issue = models.PositiveIntegerField(verbose_name='Год выпуска')
    mileage = models.PositiveIntegerField(verbose_name='Пробег, км', default=0)
    engine = models.CharField(choices=ENGINE_CHOICES,
                              max_length=30, default='not specified', verbose_name='Двигатель')
    number_of_seats = models.PositiveIntegerField(verbose_name='Количство мест')
    volume = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Объём двигателя, см3')
    power = models.PositiveIntegerField(verbose_name='Мощность, л. с.')
    transmission = models.CharField(choices=TRANSMISSION_CHOICES,
                                    max_length=20, default='not specified', verbose_name='Коробка')
    steering_wheel = models.CharField(choices=STEERING_WHEEL_CHOICES,
                                      max_length=20, default='left', verbose_name='Руль')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    created = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product-detail', kwargs={'pk': self.pk})
