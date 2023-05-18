import random

while True:
    try:

        level = int(input("Level: "))
        if level > 0:
            break

    except:
        continue


x = random.randint(1, level)


while True:

    try:

        guess = int(input("Guess: "))

        if guess > 0:

            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        continue
