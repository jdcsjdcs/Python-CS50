def main():
    meal_time = convert(input('Enter a time in format hh:mm: '))
    if 7 <= meal_time <= 8:
        print('breakfast time')
    elif 12 <= meal_time <= 13:
        print('lunch time')
    elif 18 <= meal_time <= 19:
        print('dinner time')

def convert(time):
    h,m = time.split(':')
    new_time = float(h) + float(m)/60
    return new_time


if __name__ == "__main__":
    main()