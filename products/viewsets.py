from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    '''
        get -> list ->queryset
        get -> retrieve -> product instance detail view
        post -> create -> New instance
        put -> update -> update
        path -> partial_update
        delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductGenericViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list = ProductGenericViewSet.as_view({'get':'list'})
product_detail = ProductGenericViewSet.as_view({'get':'retrieve'})