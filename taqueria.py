def main():
    # create dict os entrees menu
    menu = create_menu()
    # get from menu the item price
    total_value = 0
    while True:
        price = get_price(menu)
        if price == False: return
        total_value += price
        # print total price
        print_price(total_value)


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
        item = input("Item: ").strip().title()
        try:
            return menu[item]
        except KeyError:
            if item == '': return False

def print_price(price: float):
    price = str(price)
    if price[-1] == '0':
        price = price + '0'
    print(f'Total: ${price}')

if __name__ == '__main__':
    main()