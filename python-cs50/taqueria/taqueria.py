products = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

price = 0

while True:

    try:
        product = input('Item: ').title()
        if product in products:
            price += products[product]
            print(f'Total: ${price:.2f}')

    except EOFError:
        print()
        break
