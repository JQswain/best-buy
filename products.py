class Product:
    """The product class has attributes of name, price, quantity and if it is active"""
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            raise ValueError("Quantity must be more than 0")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """Returns the quantity of the product."""
        return self.quantity

    def get_price(self):
        """Returns the price of the product."""
        return self.price

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self):
        """Returns True if the product is active."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Shows the product in an f-string."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """changes the quantity of the product, returns the price, and runs validation"""
        if self.quantity < quantity:
            raise ValueError('Not enough in stock')
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * self.quantity


def main():
    """Test of methods"""
    bose = Product("Bose QuietComfort Earbuds", 250, 500)
    mac = Product("MacBook Air M2", 1450, 100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == "__main__":
    main()
