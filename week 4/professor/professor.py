# Import the library to use
import random

def main():
    n = get_level()
    score = 0
    problems = 0
    tries = 0

# Prompt for 10 problems
    for problems in range(10):
        x = generate_integer(n)
        y = generate_integer(n)

# Allow 3 tries
        for tries in range(3):

# Prompt the user to solve each problems
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    problems += 1
                    break

                else:
                    if answer != x + y:
# Answer incorrect --> print ("EEE") --> prompt again
                        if tries < 3:
                            print("EEE")
                            tries += 1

# After 3 incorrect tries --> Output the correct answer
                        if tries == 3:
                            print(f"{x} + {y} = {x + y}")
                            break

# Answer not a number --> print ("EEE") --> prompt again
            except ValueError:
                print("EEE")
                tries += 1
                continue

# Output the score / 10 at the end
    print("Score:", score)

def get_level():
# Induce infinite loop until the user cooperates
    while True:
        try:
# Prompt the user for a level (int)
            level = int(input("Level: "))
# If level != 1, 2 or 3 --> prompt again
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

# Generate randomly 10 math problems "X + Y ="
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

# X > 0 and Y > 0
# Additions only
