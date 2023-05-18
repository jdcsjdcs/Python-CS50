while True:

    try:
        fuel = input('Fraction: ')
        numer, denom = fuel.split('/')
        f = int(numer)/int(denom)
        if f <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

x = round(f * 100)
if x <= 1:
    print('E')
elif x >= 99:
    print('F')
else:
    print(f'{x}%')


