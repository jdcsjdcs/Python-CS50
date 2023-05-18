def main():
    greeting = input('Greating: ')
    print(f'${value(greeting)}')

def value(greeting):
    greeting = greeting.code lstrip().lower()
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()