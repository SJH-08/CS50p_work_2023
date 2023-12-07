def main():
#Induce infinite loop --> break only when user provides right input
#Prompt user for fraction's input(str)
    while True:
        try:
            fraction = convert(input("Fraction: "))
            break

        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(fraction))


def convert(fraction):
# Separate fraction into deno and num + int
    x, y = fraction.split("/")
# if not numbers
    if x.isdigit() == False or y.isdigit() == False:
        raise ValueError

# if not an int or x < y
    elif int(x) > int(y) and int(y) != 0:
        raise ValueError

# if Y is 0
    elif int(y) == 0:
        raise ZeroDivisionError
# Do the calculus
    else:
        return round(int(x) / int(y) * 100)


# Define conditions of the output (empty, full or %)
# Input = int
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
