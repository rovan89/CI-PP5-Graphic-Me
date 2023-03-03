from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=250, blank=True)
    friendly_name = models.CharField(max_length=250, null=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    size = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
