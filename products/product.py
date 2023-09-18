from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

# Create an offer Model
class Offer(models.Model):
  code = models.CharField(max_length=10)
  description = models.CharField(max_length=255)
  discount = models.FloatField()

