def main():
    # create dict os entrees menu
    menu = create_menu()
    # get from menu the item price
    price = get_price(menu)
    # print price of item
    print_price(price)
    return

def create_menu():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    return menu

def get_price(menu: dict):
    while True:
        item = input("Item: ").strip().lower()
        try:
            return menu[item]
        except KeyError:
            pass

def print_price(price: float):
    print(f'${price}')

if __name__ == '__main__':
    main()