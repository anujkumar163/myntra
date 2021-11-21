from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	catname = models.CharField(max_length=50)


class Products(models.Model):
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=12, decimal_places=2)
	qty = models.IntegerField()
	pro_img = models.ImageField(upload_to='productimage', blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)