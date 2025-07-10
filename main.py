import products
import store


#set up of initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
                 ]
best_buy = store.Store(product_list)

def list_products(store_object):
    """lists the products available for the user"""
    inactive = [p for p in store_object.get_all_products() if p.get_quantity() == 0]
    for product in inactive:
        store_object.remove_product(product)

    for i, product in enumerate(store_object.get_all_products(), 1):
        print(f"{i}. {product.show()}")


def total_quantity(store_object):
    """Shows the total quantity of products in the store for the user"""
    print(f"Total of {store_object.get_total_quantity()} products in store")

def make_order(store_object):
    """calls on store and product object methods to place ab order"""

    shopping_list = []
    list_products(store_object)
    available_products = store_object.get_all_products()

    while True:
        product_choice = (input("""
When you would like to finish the order please type 'e' for end.
Enter product number you would you like to buy: 
"""))
        if product_choice.lower() == "e":
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(available_products):
                print("Invalid product number.")
                continue
            product = available_products[product_index]
        except ValueError:
            print("Please enter a valid number.")
            continue

        quantity_choice = int(input("""In what amount? """))
        if product.get_quantity() < quantity_choice:
            print(f"Sorry, this product has only {product.get_quantity()} left")
            continue

        shopping_list.append((product, quantity_choice))
        print("Order added to shopping list!")
    if shopping_list:
        total_price = store_object.order(shopping_list)
        print(f"Order placed! Total payment: ${total_price}")
    else:
        print("No items were ordered.")


def start(store_object):
    """Shows the user interface and access pre-defined functions"""
    store_actions = {
        "1": ("List all products", list_products),
        "2": ("Show total amount", total_quantity),
        "3": ("Make an order", make_order),
    }
    while True:
        print("""
                 Store Menu
            --------------------
        1. List all products in store
        2. Show total amount in store 
        3. Make an order
        4. Quit
        """)
        choice = input("Enter your choice between 1-4: ")
        store_actions[choice][1](store_object)
        input("Press enter to continue...\n")
        if choice == "4":
            break

start(best_buy)
