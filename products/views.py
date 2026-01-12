from rest_framework import authentication, generics,mixins, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.permissions import IsStaffEditorPermission
# from django.http import http404
from django.shortcuts import get_object_or_404
from api.authentication import TokenAuthentication
from api.mixins import (StaffEditorPermissionMixin, UserQuerysetMixin)

class ProductCreateAPIView(generics.CreateAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        email = serializer.validated_data.pop('email')
        print(email)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' -----> Product.objects.get(pk)

product_detail_view = ProductDetailAPIView.as_view()

class ProductDetailAPIView(generics.ListAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_detail_view = ProductDetailAPIView.as_view()


class ProductListCreateAPIView(StaffEditorPermissionMixin,
                               UserQuerysetMixin,
                               generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(request.user)
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()




# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None,*args,**kwargs):
#     if request.method == 'GET':
#         # get request -> detal view
#         #  list view
#         if pk is not None:
#             # detail view
#             # qs = Product.objects.filter(pk=pk)
#             # if not qs.exists():
#             #     raise Http404
#             # return Response()
#             # or
#             obj = get_object_or_404(Product,pk=pk)
#             data = ProductSerializer(obj,many = False).data
#             return Response(data)
#         # list view
#         qs = Product.objects.all()
#         data = ProductSerializer(qs,many=True).data
#         return Response(data)
#     elif request.method == 'POST':
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid":"not good data"},status=400)
#     return product_create_view(request)


class ProductUpdateAPIView(generics.UpdateAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #-----> Product.objects.get(pk)
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(generics.DestroyAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #-----> Product.objects.get(pk)
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView,StaffEditorPermissionMixin):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#     def get(self,request,*args,**kwargs):
#         print(args,kwargs)
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# product_mixin_view = ProductMixinView.as_view()