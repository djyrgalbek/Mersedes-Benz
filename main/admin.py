from django.contrib import admin

from .models import *

# Регистрация моделей в админку
admin.site.register(Category)
admin.site.register(Product)

