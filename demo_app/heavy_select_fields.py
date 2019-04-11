from django.utils.translation import ugettext_lazy as _
from django_select2.forms import ModelSelect2Widget
from . import models


class BaseHeavySelect2Widget(ModelSelect2Widget):
    def build_attrs(self, *args, **kwargs):
        attrs = super(BaseHeavySelect2Widget, self).build_attrs(*args, **kwargs)
        attrs['data-placeholder'] = _('Type at least 2 characters to search')
        attrs['data-width'] = '21em'
        return attrs


class CollectionModelWidget(BaseHeavySelect2Widget):
    model = models.Collection
    search_fields = ['name__icontains']
