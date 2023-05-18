import validators

def main():
    print(validate(input("Text: ")))

def validate(email):
    if validators.email(email):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__":
    main()
