from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SaleViewSet, validate_cart

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'sales', SaleViewSet, basename='sale')

urlpatterns = [
    path('', include(router.urls)),
    path('validate-cart', validate_cart, name='validate_cart'),
]

