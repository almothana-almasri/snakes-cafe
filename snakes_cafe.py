def print_intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
''')


def print_menu():
    menu = {
        "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
        "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
        "Desserts": ["Ice Cream", "Cake", "Pie"],
        "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
    }

    for category, items in menu.items():
        print(category)
        print("-" * 10)
        for item in items:
            print(item)
        print()

    return menu


print_intro()
menu = print_menu()
orders = {}


def is_valid_item(order, menu):
    for items in menu.values():
        if order in items:
            return True
    return False


def process_order(order, menu):
    if is_valid_item(order, menu):
        if order in orders:
            orders[order] += 1
            print(
                f"** {orders[order]} orders of {order} have been added **")
        else:
            orders[order] = 1
            print(f"** 1 order of {order} has been added **")
    else:
        print(f"** {order} is not on the menu, but we'll send you a Mansaf instead! **")


def print_order_summary(orders):
    print("\nOrder Summary:")
    for item, count in orders.items():
        print(f"{count} x {item}")


def main():
    while True:
        order = input('''
***********************************
** What would you like to order? **
***********************************
> ''')
        if order.lower() == "quit":
            print_order_summary(orders)
            break
        process_order(order, menu)


if __name__ == "__main__":
    orders = {}
    main()