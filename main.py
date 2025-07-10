import products
import store


#set up of initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
                 ]
best_buy = store.Store(product_list)

def list_products(store_object):
    for i, product in enumerate(store_object.get_all_products(), 1):
        print(f"{i}. {product.show()}")

def total_quantity(store_object):
    print(f"Total of {store_object.get_total_quantity()} products in store")

def make_order(store_object):
    shopping_list = []
    product_list = store_object.get_all_products()
    list_products(store_object)
    while True:
        product_choice = (input(f"""
When you would like to finish the order please type 'e' for end.
Enter product number you would you like to buy: """))
        if product_choice == "e":
            break

        quantity_choice = int(input("""In what amount? """))
        shopping_list.append((product_list[int(product_choice) -1], quantity_choice))
        print("Order added to shopping list!")
    total_price = store_object.order(shopping_list)
    print(f"Order placed! Total payment: ${total_price}")


def start(store_object):
    store_actions = { "1": list_products,
                      "2": total_quantity,
                      "3": make_order,
    }
    while True:
        print(f"""
                 Store Menu
            --------------------
        1. List all products in store
        2. Show total amount in store 
        3. Make an order
        4. Quit
        """)
        choice = input("Enter your choice between 1-4: ")
        store_actions[choice](store_object)
        input("Press enter to continue...\n")
        if choice == "4":
            break

start(best_buy)