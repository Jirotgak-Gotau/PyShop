  # Import necessary modules
from django.db import models
from django.contrib.auth.models import User  # If you're using Django's built-in user model


# Create the Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the cart to a user
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Link the cart to a product
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product

    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.product.name}"

# Create the Product Model as well
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

  
  