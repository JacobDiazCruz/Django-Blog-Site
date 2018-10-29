from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Cart
import re


@login_required()
def cart_pending_orders(request):
	#fetch the user
	user_ordered = get_object_or_404(Profile, user=request.user)
	#fetch the Order model
	order = Cart.objects.filter(user=user_ordered, is_ordered=False)
	if order.exists():
		# get only the order in the list of filtered orders
		return order[0]
	return 0

@login_required()
def add_to_cart(request, **kwargs):
	user_ordered = Profile.objects.all()