from django.contrib import admin
from .models import Cat

# Регистрация модели Cat в админке
admin.site.register(Cat)
