from rest_framework import serializers
# from products.serializers import ProductSerializer(There is a circular import happening in here)
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail'
    ,lookup_field='pk',read_only=True)
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'this_is_not_real', #this is not cuasing any issues
            'id',
        ]

    def get_other_products(self,obj):
        request = self.context.get('request')
        print(obj)
        user = obj
        my_products_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data
    