import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Category, Product
from profiles.models import UserProfile

CONCEPT_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Order(models.Model):
    """ This is a model of a customers order """

    id = models.BigAutoField(primary_key=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="user_order")
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="orders")
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True,)
    image = models.ImageField(null=True, blank=True)
    number_of_concepts = models.IntegerField(choices=CONCEPT_CHOICES)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery cost
        """
        self.grand_total

    def save(self, *args, **kwargs):
        """" Override original save method and set order number """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderDesignItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='designitems')
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=False, blank=False, on_delete=models.CASCADE)
    design_order_total = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=False, blank=False, editable=False)

    def _generate_item_number(self):
        """ Generate a random, unique order number using UUID """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """" Override original save method and set order number """
        if not self.item_number:
            self.item_number = self._generate_item_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_number

    def save(self, *args, **kwargs):
        self.design_order_total = self.category.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product.id} on order {self.order.order_number}'
