from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.serializers import ProductSerializer, ProductSerializerMinimized
from products.service import create_product, delete_product, get_all_products, get_one, update_product

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

@api_view(["GET"])
def get_one_view(request):
    id = request.query_params.get("id")
    product = get_one(id)

    if product is None:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)

    return Response(serializer.data)

@api_view(["PUT"])
def put_view(request):
    product = update_product(
        id=request.data["id"],
        name=request.data["name"],
        volume=request.data["volume"],
        brand=request.data["brand"],
        quantity=request.data["quantity"],
        price=request.data["price"],
    )
    if product is None:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_view(request):
    id = request.query_params.get("id")
    if delete_product(id=id):
        return Response(
                    {},
                    status=status.HTTP_204_NO_CONTENT
                )
    else:
        return Response(
                    {"error": "Product not found"},
                    status=status.HTTP_404_NOT_FOUND
                )