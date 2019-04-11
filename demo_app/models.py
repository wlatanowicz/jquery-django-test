from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
