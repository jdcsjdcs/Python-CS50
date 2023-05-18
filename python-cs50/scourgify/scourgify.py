import sys
import csv

def main():

    check_arg()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            with open(sys.argv[2], 'w') as new_file:
                writer = csv.DictWriter(new_file, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    names = row['name'].split(',')
                    house = row['house']
                    first_name = names[1].lstrip()
                    last_name = names[0].lstrip()
                    writer.writerow({'first':first_name, 'last':last_name, 'house': house })
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()