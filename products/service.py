from .models import Product
from django.db import transaction


def create_product(name, brand, volume, price, quantity):
    if len(name) == 0:
            raise ValueError("name mustt not be blank")
    
    if len(brand) == 0:
            raise ValueError("name mustt not be blank")

    if volume <= 0:
        raise ValueError("invalid volume")
    
    if price <= 0:
        raise ValueError("invalid price")

    if quantity <= 0:
        raise ValueError("invalid quantity")

    return Product.objects.create(
         name=name,
         brand=brand,
         volume=volume,
         price=price,
         quantity=quantity
    )

def get_all_products():
    return Product.objects.all()

def get_one(id):
    try:
        return Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return None


@transaction.atomic
def update_product(id, name, brand, volume, price, quantity):

    if len(name) == 0:
        raise ValueError("name mustt not be blank")
    
    if len(brand) == 0:
            raise ValueError("name mustt not be blank")

    if volume <= 0:
        raise ValueError("invalid volume")
    
    if price <= 0:
        raise ValueError("invalid price")

    if quantity <= 0:
        raise ValueError("invalid quantity")

    try:
        product = Product.objects.select_for_update().get(pk=id)

        product.name = name
        product.brand = brand
        product.volume = volume
        product.price = price
        product.quantity = quantity

        product.save()

        return product

    except Product.DoesNotExist:
        return None