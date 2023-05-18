def main():
    calculation = calculator(input('Enter a number, operator( +, -, *, or /) and an other number(like 1 * 2): '))
    print(f'{calculation:.1f}')

def calculator(str):
    x, y, z = str.split()
    x = float(x)
    z = float(z)
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    else:
        return x / z

main()