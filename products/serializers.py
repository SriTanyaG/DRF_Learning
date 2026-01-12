from rest_framework import serializers
from rest_framework.reverse import reverse
from django import forms
from .validators import validate_title_no_hello,unique_product_title
from .models import Product
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail'
    ,lookup_field='pk',read_only=True)
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
        owner = UserPublicSerializer(source='user',read_only=True)
        # related_products = ProductInlineSerializer(source = 'user.product_set.all',many=True,read_only=True)
        my_user_data = serializers.SerializerMethodField(read_only=True)
        # discount = serializers.SerializerMethodField(read_only=True)
        edit_url = serializers.SerializerMethodField(read_only=True)
        url = serializers.HyperlinkedIdentityField(view_name='product-detail'
        ,lookup_field='pk',read_only=True)
        email = serializers.EmailField(write_only=True)
        title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title]) 
        name = serializers.CharField(source='title',read_only=True)
        class Meta:
            model = Product
            fields = ['owner',
                      'url',
                      'edit_url',
                      'email',
                      'pk',
                      'title',
                      'name',
                      'content',
                      'price',
                      'sale_price',
                    #   'discount',
                      'my_user_data',
                      #'related_products',
                      ]
        
        def get_my_user_data(self, obj):
             return {
                  "username":obj.user.username
            }


        # def validate_title(self, value):
        #     request = self.context.get('request')
        #     user = request.user
        #     qs = Product.objects.filter(title__iexact=value)
        #     if qs.exists():
        #             raise serializers.ValidationError(f"{value} is already a product name")
        #     return value
                
        
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

        # def validate_title(self,value):  #validate_<field_name>
        #     qs = Product.objects.filter(title__iexact=value)
        #     if qs.exists():
        #          raise serializers.ValidationError(f"{value} is already a product name")
        #     return value
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
        