from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSets

router = DefaultRouter()
router.register('products-abc', ProductViewSets, 'product')
print(router.urls)
urlpatterns = router.urls