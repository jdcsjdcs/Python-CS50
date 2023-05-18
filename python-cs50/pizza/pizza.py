import sys
import csv
import tabulate

def main():

    check_arg()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers='keys',tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit(" Not a CSV file")

if __name__ == "__main__":
    main()