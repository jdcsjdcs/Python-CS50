import random


def main():

    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x in [1, 2, 3]:
                return x
                break
        except ValueError:
            continue


def generate_integer(level):
    score = 0

    for i in range(10):
        tries = 0

        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        while True:

            solution = int(input(f"{x} + {y} = "))
            if solution == x + y:
                score += 1
                break

            elif solution != x + y:
                tries += 1
                print("EEE")

                if tries == 3:
                    print(f"{x} + {y} = {x + y}")
                    break

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
