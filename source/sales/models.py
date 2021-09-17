from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.shortcuts import reverse
from products.models import Product
from customers.models import Customer
from profiles.models import Profiles
from .utils import generate_code

# position = quantity and prices for products
# two position can have the same product name
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name


# Sale can have many Position
# depend when the position is sold 
class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return " transaction id {} with total price {}".format(self.transaction_id, self.total_price)

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name