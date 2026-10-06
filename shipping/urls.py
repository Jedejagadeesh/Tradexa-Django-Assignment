from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, BoxViewSet


router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('boxes', BoxViewSet)


urlpatterns = [
    path('', include(router.urls)),
]