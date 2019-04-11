from django import forms

from . import heavy_select_fields
from . import models


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'collection': heavy_select_fields.CollectionModelWidget,
        }
