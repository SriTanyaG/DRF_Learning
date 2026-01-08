import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response    
from products.serializers import ProductSerializer

# def api_home(request,*args, **kwargs):
#     # # To extract diferrent parts of data from request
#     # # JSON
#     # # Request is an instance of HTTP request, which is completely different from python requests
#     # # request.body is a byte string of JSON
#     # # 
#     # body = request.body
#     # data = {}
#     # try :
#     #     data = json.loads(body)   #String of json to python dict #it will get the query part
#     # except:
#     #     pass
#     # print(data)
#     # print(request.headers)
#     # print(request.GET) # url query params
#     # print(request.POST) #will be empty for post request
#     # data['params'] = dict(request.GET)
#     # data['headers'] = dict(request.headers) # headers are not json serializable need to be converted to dict
#     # data['content_type'] = request.content_type
#     # return JsonResponse(data)

#     model_data = Product.objects.all().order_by("?").first()  #get the first random product from database
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # model instance(model_data)
#         # turn a python dict
#         # return JSON to my client

#         # directly to dict
#         data = model_to_dict(model_data)
#         json_data_str = json.dumps(data)

#         # Serialization
#     return HttpResponse(json_data_str ,headers={'content-type':'application/json'})


# Decorator
# Able to change the function logic, without touching the function

# def div(a,b):
#     print(a/b)
# def smart_div(func):
#     def inner(a,b): #Same numbuer of arguments as func
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return inner
# # Block 1
# div1 = smart_div(div)
# div1(2,4)
# # Block 2
# @smart_div
# def div(a,b):
#     print(a/b)

# div(2,4)

# # Both Block 1 and 2 are same


# # Block 1
# @decorator_name
# def add(a, b):
#     return a + b
# # Block 2
# def add(a, b):
#     return a + b

# add = decorator_name(add)
# Both block 1 and 2 are same
# Djanjo rest framewok view

@api_view(['GET'])
def api_home(request,*args,**kwargs):
    """
    DRF API View
    """
    # if request.method != "POST":
    #     return Response({"detail":"get NOT ALLOWED"},status = 405)
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
    # return Response(data)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)

@api_view(['POST'])
def api_home(request,*args,**kwargs):
    """
    DRF API View
    """
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        # data = serializer.data
        return Response(serializer.data)
