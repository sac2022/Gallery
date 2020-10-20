import django_filters

from gallery.models import ImageModel


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ImageModel
        fields = ['category']