import products

class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Adds a new product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """returns the total quantity of all products in the store"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self) -> list[products.Product]:
        """returns a list of all products in the store"""
        product_list = []
        for product in self.products:
            if product.is_active():
                product_list.append(product)
        return product_list

    def order(self, shopping_list) -> float | None:
        """Updates the quantity of products and returns a total price for the quantity in the order"""
        total_price = 0
        for product, quantity in shopping_list:
            product.buy(quantity)
            total_price += product.get_price() * quantity

        return total_price

def main():
    product_list = [products.Product("MacBook Air M2", 1450, 100),
                    products.Product("Bose QuietComfort Earbuds", 250, 500),
                    products.Product("Google Pixel 7", 500, 250),
                    ]

    best_buy = Store(product_list)
    available_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(available_products[0], 1), (available_products[1], 2)]))

if __name__ == "__main__":
    main()
