from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product


@register(Product)
class ProductsIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public',

    ]
    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user', 'public'],
    }
    tags = 'get_tags_list'
# These are the filed i want to show in the search, algolia we take the models.py data nad map it with the filed mentioned over here