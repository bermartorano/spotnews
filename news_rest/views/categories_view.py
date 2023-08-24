from rest_framework import viewsets
from ...news.models.category_model import Categories
from ..serializers.categories_serializer import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
