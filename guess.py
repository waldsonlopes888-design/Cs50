import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
    except ValueError:
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break
