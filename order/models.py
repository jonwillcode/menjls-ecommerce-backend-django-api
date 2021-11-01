import random
import string
from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    ORDER_STATUS_SUBMITTED = 'S'
    ORDER_STATUS_CANCELLED = 'X'
    ORDER_STATUS_COMPLETED = 'C'
    ORDER_STATUS_READY = 'R'

    ORDER_CHOICES = [
        (ORDER_STATUS_SUBMITTED, 'Submitted'),
        (ORDER_STATUS_CANCELLED, 'Cancelled'),
        (ORDER_STATUS_READY, 'Ready for pickup'),
        (ORDER_STATUS_COMPLETED, 'Completed'),
    ]

    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    postal = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, default=ORDER_STATUS_SUBMITTED, choices=ORDER_CHOICES)
    pickup_time = models.TimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.first_name} {self.last_name}\'s {self.get_status_display()} order'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'
