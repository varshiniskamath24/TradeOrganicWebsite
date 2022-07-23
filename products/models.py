from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    price = models.FloatField()
    dueDate = models.DateField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=2083)

