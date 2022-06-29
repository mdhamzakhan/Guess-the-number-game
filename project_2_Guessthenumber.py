import random 

number = random.randint(1, 11)

def guess():
    guess = 0

    while number != guess:
        guess = int(input("enter your guess between 1 to 10 "))
        if guess > number:
            print("too high, guess a lesser number")
        elif guess< number:
            print("too low, guess a higher number")

    print(F"CONGRATS! you won, the number was {number} ")

guess()
