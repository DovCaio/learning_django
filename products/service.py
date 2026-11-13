from .models import Product

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

    