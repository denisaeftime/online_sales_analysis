from product import Product
from product_manager import ProductManager

pm = ProductManager()

# Adăugarea unor produse
p1 = Product("Laptop", 3500, 10)
p2 = Product("Mouse", 100, 50)
p3 = Product("Keyboard", 150, 30)

pm.add_product(p1)
pm.add_product(p2)
pm.add_product(p3)

# Afișarea produselor
pm.display_products()

# Afișarea valorii totale a inventarului
print(f"Total inventory value: {pm.total_inventory_value()}")
