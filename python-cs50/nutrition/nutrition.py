table = {'apple': 130,
         'avocado': 50,
         'banana': 110,
         'cantaloupe': 50,
         'grapefruit': 60,
         'grapes': 90,
         'honeydew Melon': 50,
         'kiwifruit': 90,
         'lemon': 15,
         'lime': 20,
         'nectarine': 60,
         'orange': 80,
         'peach': 60,
         'pear': 100,
         'pineapple': 50,
         'plums': 70,
         'strawberries': 50,
         'sweet cherries': 100,
         'Tangerine': 50,
         'Watermelon': 80}

fruit = input('Enter a fruit name: ').lower()

if fruit in table:
    print(f'Calories: {table[fruit]}')