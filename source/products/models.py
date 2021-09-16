from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products", default="default.png")
    price = models.FloatField(help_text="dalam Ratusan Ribu Rupiah (IDN)")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} has been added with price Rp.{} (ratus ribu)".format(self.name, self.price)