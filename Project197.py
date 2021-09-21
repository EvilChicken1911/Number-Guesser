import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9:")
while chances < 3:
    guess = int(input("Guess a number:"))
    if guess == number:
        print("Congradulations you win")
        break
    elif guess > number:
        print("Your guess was too high, guess a smaller number")
    else:
        print("Your guess was too low, try a bigger number")
    chances +=1
if not chances < 3:
    print("You lose")
