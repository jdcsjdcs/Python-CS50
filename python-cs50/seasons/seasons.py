from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
    b_date = input('Your birthday: ')
    try:
        year, month, day = validate(b_date)
    except:
        sys.exit('Invalid Date')
    form_b_date = date(int(year), int(month), int(day))
    age_in_min = (date.today() - form_b_date) * 24 * 60
    words = p.number_to_words(age_in_min.days, andword="")
    print(f'{words.capitalize()} minutes')

def validate(b_date):
    if re.search(r'^\d{4}-\d{2}-\d{2}$', b_date):
        year, month, day = b_date.split('-')
        return year, month, day


if __name__ == "__main__":
    main()