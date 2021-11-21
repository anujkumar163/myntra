from django.db import models
from seller.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):

	class Meta():
		unique_together = ('user', 'product')

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Products, on_delete=models.CASCADE)