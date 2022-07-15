from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    friendly_name = models.CharField(max_length=250, null=False, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category',null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    size = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    number_of_concepts = models.IntegerField(default=1)
    number_of_designs = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
