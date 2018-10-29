from django.db import models
from products.models import Product
from users.models import Profile
from django.urls import reverse

class OrderItem(models.Model):
	product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
	date_added = models.DateTimeField(auto_now=True)
	is_ordered = models.BooleanField()

	def __str__(self):
		return self.Products

class Cart(models.Model):
	product = models.ManyToManyField(OrderItem)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	is_ordered = models.BooleanField()
	date_ordered = models.DateTimeField(auto_now=False)

	def get_cart_items(self):
		return self.items.all()