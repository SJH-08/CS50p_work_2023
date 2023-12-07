# Import library to use
import random
import sys

# Induce infinite loop until user cooperates
while True:

# Prompt user for an int
# check if input is a number and convert into an int
    try:
        n = input("Level: ")
        if n.isdigit():
            n = int(n)

# Check if int > 0 --> break
# Generate a random 1 < int < n (r)
            if n > 0:
                r = random.randint(1, n)
                break

# Otherwise prompt again
    except ValueError:
        continue

# Induce infinite loop until user cooperates
while True:
# Prompt the user to guess the int
# check if input is a number and convert into an int
    try:
        g = input("Guess: ")
        if g.isdigit():
            g = int(g)
# Check if int > 0
            if g > 0:
# if guess > r: too large --> prompt again
                if g > r:
                    print("Too large!")
# if guess < r: too small --> prompt again
                elif g < r:
                    print("Too small!")
# if guess == r: just right --> exit
                elif g == r:
                    sys.exit("Just right!")

# if guess < 0: prompt again
    except ValueError:
        continue
