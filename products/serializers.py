from rest_framework import serializers
from django import forms

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
        discount = serializers.SerializerMethodField(read_only=True)
        class Meta:
            model = Product
            fields = ['title','content','price','sale_price','discount']
        def get_discount(self, obj):
            # print(obj.id)
            # try:
            #     return obj.get_discount()
            # except:
            #     return None
            if not hasattr(obj,'id'):
                 return None
            if not isinstance(obj,Product):
                return None
            return obj.get_discount()
        