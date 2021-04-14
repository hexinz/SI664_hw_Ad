from django.contrib import admin

# Register your models here.

from .models import Auto, Make

admin.site.register(Make)
admin.site.register(Auto)