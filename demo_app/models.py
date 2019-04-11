from django.db import models
from filer.fields.image import FilerImageField


class Collection(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = FilerImageField(blank=True, null=True, on_delete=models.CASCADE)
