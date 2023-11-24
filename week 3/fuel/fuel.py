# Define conditions of the output (empty, full or %)
def main():
    fuel = get_fraction()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_fraction():
#Induce infinite loop --> break only when user provides right input
#Prompt user for fraction's input(str)
    while True:
        prompt = input("Fraction: ")
# separate fraction into deno and num + int
        try:
            x, y = prompt.split("/")
            num = int(x)
            den = int(y)
# Check x < y + do the calculus
            if num <= den:
                return round(num / den * 100)

# if not an int or Y is 0
        except (ValueError, ZeroDivisionError):
            pass

main()
