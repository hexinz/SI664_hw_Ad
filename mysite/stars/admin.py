from django.contrib import admin

# Register your models here.
from .models import Type, Star

admin.site.register(Type)
admin.site.register(Star)