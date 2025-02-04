class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if product.quantity >= quantity:
            self.cart_items.append((product, quantity))
            product.update_quantity(product.quantity - quantity)
        else:
            print("Not enough stock available!")

    def display_cart(self):
        for product, quantity in self.cart_items:
            print(f"{product.name} - {quantity}")

    def total_cart_value(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)
