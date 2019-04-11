from parler.forms import TranslatableModelForm

from . import heavy_select_fields
from . import models


class ProductAdminForm(TranslatableModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'collection': heavy_select_fields.CollectionModelWidget,
        }
