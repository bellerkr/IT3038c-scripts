import random
x = random.randint(1,100)
guess = int(input("Guess a number from 1 - 100: "))

while x != "guess":
    print
    if guess < x:
        print("Your guess was too low.")
        guess = int(input("Guess a number from 1 - 100: "))

    elif guess > x:
        print ("your guess is too high")
        guess = int(input("Guess a number from 1 - 100: "))

    else:
        print("You guessed the number!")
        break
    print

