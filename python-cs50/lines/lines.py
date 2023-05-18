import sys

def main():
    check_arg()

    try:
        with open(sys.argv[1]) as file:
            lines = 0
            for line in file:
                if not line.lstrip().startswith('#') and line.lstrip() != '':
                    lines += 1

        print(lines)

    except FileNotFoundError:
        sys.exit('File does not exist')


def check_arg():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif '.py' not in sys.argv[1]:
        sys.exit(' Not a Python file')




if __name__ == '__main__':
    main()