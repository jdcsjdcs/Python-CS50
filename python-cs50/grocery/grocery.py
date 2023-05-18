grocery_list = {}

while True:

    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        for key, value in sorted(grocery_list.items()):
            print(grocery_list[key], key)
        break