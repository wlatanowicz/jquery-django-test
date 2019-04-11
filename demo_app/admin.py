from django.contrib import admin
from . import models
from . import forms


admin.site.register(models.Collection)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('//code.jquery.com/jquery-3.3.1.min.js',)

    fieldsets = [
        ('Required data', {
            "fields": [
                'name',
                'collection',
                'image',
                ]
        })
    ]
    form = forms.ProductAdminForm
