from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    region = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.region


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    blend = models.CharField(max_length=254)
    age = models.PositiveSmallIntegerField(null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField(default=0, null=True, blank=True)
    is_exclusive = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
