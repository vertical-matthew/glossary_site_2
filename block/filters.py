"""WIP"""
import django_filters
from .models import *

#https://www.youtube.com/watch?v=G-Rct7Na0UQ


class BlockFilter(django_filters.FilterSet):
    class Meta:
        material = Material
        # category =
        # condition =
        # tags =
