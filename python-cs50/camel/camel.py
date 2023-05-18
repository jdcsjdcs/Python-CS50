camel_case = input('Camel case: ')
print('Snake case: ', end='')
for letter in camel_case:
    if letter.isupper():
        print('_' f'{letter.lower()}', end='')
    else:
        print(letter, end='')
