greating = input('Greating: ').lstrip().lower()

if greating.startswith('hello'):
    print('$0')
elif greating.startswith('h'):
    print('$20')
else:
    print('$100')