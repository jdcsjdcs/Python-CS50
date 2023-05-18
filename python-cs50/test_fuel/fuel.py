
def main():
    fuel = input('Fraction: ')
    print(gauge(convert(fuel)))



def convert(fuel):
    while True:
        try:

            numer, denom = fuel.split('/')
            f = round(int(numer) / int(denom) * 100)
            if f <= 100:
                return f

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()




