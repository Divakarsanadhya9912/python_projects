import random

num = random.randint(1,10)
guess = 0

while guess != num:
    guess = int(input("Guess a no. between 1 to 10:"))
    if guess < num:
        print("guess higher")
    elif guess > num:
        print("guess lower")
    else:
        print("you win")