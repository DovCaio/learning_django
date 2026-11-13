from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.serializers import ProductSerializer
from products.service import create_product, get_all_products

@api_view(["POST"])
def create_product_view(request):
    try:
        product = create_product(   name=request.data["name"],
            brand=request.data["brand"],
            volume=request.data["volume"],
            quantity=request.data["quantity"],
            price=request.data["price"]
        )

        return Response(
            {"id": product.id},
            status=status.HTTP_201_CREATED
        )
    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(["GET"])
def get_all_view(_):
    products = get_all_products()
    serializer = ProductSerializer(products, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )
