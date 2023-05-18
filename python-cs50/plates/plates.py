def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7 and s[0:2].isalpha() and s.isalnum():
        for i in range(2, len(s)-1):
            if (s[i].isdigit() and not s[i+1].isdigit()) or (s[i] == '0' and s[i-1].isalpha()):
                return False
        return True

    return False

main()