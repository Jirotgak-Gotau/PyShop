from django.db import models

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey('Product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
