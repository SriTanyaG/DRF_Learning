from django.urls import path
from .import views

# path with "/" will give us, a url as api/products//, so we eed to avoid i t and keep it empty
urlpatterns = [
    # path("",views.product_list_detail_view),
    # path("",views.product_alt_view),
    # path("<int:pk>/",views.product_alt_view),
    path("",views.product_list_create_view,name = 'product-list'),
    # path("",views.product_create_view),
    # path("<int:pk>/",views.ProductDetailAPIView.as_view())
    # path("",views.product_list_create_view),
    # path('',views.product_mixin_view),
    # path('<int:pk>/',views.product_mixin_view),
    path("<int:pk>/update/",views.product_update_view, name='product-edit'),
    path("<int:pk>/delete/",views.product_destroy_view),
    # path("<int:pk>/delete/",views.product_detail_view),
    path("<int:pk>/",views.product_detail_view, name = 'product-detail'),  #<model_name>_detail(as it is a detail view)

]