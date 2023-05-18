import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$', s):
        if time.group(2) or time.group(5):
            if int(time.group(2)) > 59 or int(time.group(5)) > 59:
                raise ValueError

        #start time
        first_hour = int(time.group(1))
        if time.group(3) == 'PM' and first_hour != 12:
            first_hour += 12
        elif time.group(3) == 'AM' and first_hour == 12:
            first_hour -= 12
        if time.group(2):
            first_time = f'{first_hour:02}:{time.group(2)}'
        else:
            first_time = f'{first_hour:02}:00'

        #finish time
        second_hour = int(time.group(4))
        if time.group(6) == 'PM' and second_hour != 12:
            second_hour += 12
        elif time.group(6) == 'AM' and second_hour == 12:
            second_hour -= 12
        if time.group(5):
            second_time = f'{second_hour:02}:{time.group(5)}'
        else:
            second_time = f'{second_hour:02}:00'

        return(f'{first_time} to {second_time}')

    else:
        raise ValueError

if __name__ == "__main__":
    main()