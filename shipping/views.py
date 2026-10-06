from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Order, Box
from .serializers import ProductSerializer, OrderSerializer, BoxSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'], url_path='calculate-boxes')
    def calculate_boxes(self, request, pk=None):
        order = self.get_object()

        products = order.products.all()
        boxes = Box.objects.all()

        if not products:
            return Response(
                {"error": "Order has no products"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total_weight = sum(product.weight for product in products)

        suitable_boxes = []

        for box in boxes:

            if total_weight > box.max_weight:
                continue

            all_products_fit = True

            for product in products:

                if (
                    product.length > box.length
                    or product.width > box.width
                    or product.height > box.height
                ):
                    all_products_fit = False
                    break

            if all_products_fit:
                suitable_boxes.append({
                    "id": box.id,
                    "name": box.name,
                    "length": box.length,
                    "width": box.width,
                    "height": box.height,
                    "max_weight": box.max_weight
                })

        return Response({
            "order_id": order.id,
            "total_weight": total_weight,
            "suitable_boxes": suitable_boxes
        })


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer