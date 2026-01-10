from rest_framework import serializers
from rest_framework.reverse import reverse
from django import forms

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
        discount = serializers.SerializerMethodField(read_only=True)
        edit_url = serializers.SerializerMethodField(read_only=True)
        url = serializers.HyperlinkedIdentityField(view_name='product-detail'
        ,lookup_field='pk',read_only=True)

        email = serializers.EmailField(write_only=True)
        class Meta:
            model = Product
            fields = ['url','edit_url','email','pk','title','content','price','sale_price','discount']
        
        def create(self, validated_data):
            # return Product.objects.create(**validated_data)
            email = validated_data.pop('email')
            obj = super().create(validated_data)
            print(email,obj)
            return obj
        def update(self, instance, validated_data):
            instance.title =validated_data.get('title')
            return instance


        # def get_url(self, obj):
        #     # return f"/api/v2/products/{obj.id}"
        #     request = self.context.get('request')
        #     if request is None:
        #          return None
        #     return reverse("product-detail",kwargs={'pk':obj.pk},request=request)
        def get_edit_url(self, obj):
            # return f"/api/v2/products/{obj.id}"
            request = self.context.get('request')
            if request is None:
                 return None
            return reverse("product-edit",kwargs={'pk':obj.pk},request=request)
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
        