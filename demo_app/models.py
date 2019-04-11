from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class Collection(models.Model):
    name = models.CharField(max_length=250)


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description = RichTextField(),
    )

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = FilerImageField(blank=True, null=True, on_delete=models.CASCADE)

    date = models.DateTimeField(null=True)
