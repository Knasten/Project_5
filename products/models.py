from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=32)
    friendly_name = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.IntegerField(null=True, blank=True, unique=True)
    name = models.TextField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField(null=True, blank=True)
    make = models.CharField(max_length=64)
    model_id = models.CharField(max_length=64)


    def __str__(self):
        return self.name
