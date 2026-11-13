from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.service import create_product

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
    
