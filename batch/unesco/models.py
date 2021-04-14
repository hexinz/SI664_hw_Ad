from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, null=True)
    justification = models.CharField(max_length=512, null=True)
    year = models.IntegerField(null=True)
    # longitude = models.CharField(max_length=32, null=True)
    # latitude = models.CharField(max_length=32, null=True)
    # area_hectares = models.CharField(max_length=32, null=True)

    # longitude = models.DecimalField(max_digits=9, decimal_places=5,null=True)
    # latitude = models.DecimalField(max_digits=9, decimal_places=5,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=5,null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=5,null=True)
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # location = models.ForeignKey("Location", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    iso = models.ForeignKey("Iso", on_delete=models.CASCADE)
    # location = models.ForeignKey("Location", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=32, unique=True)
    iso = models.ForeignKey("Iso", on_delete=models.CASCADE)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=2, unique=True)
    def __str__(self):
        return self.name


