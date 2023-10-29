# Ask user's input (str)
exp = input("Enter a calculus: ")

# Split the calculus into 3 variables (str)
x1, y1, z1 = exp.split(" ")

# Convert str into float
x2 = float(x1)
z2 = float(z1)

# Calculate and round to 1 decimal
match y1:
    case "+":
        print(round(x2 + z2,1))
    case "-":
        print(round(x2 - z2,1))
    case "*":
        print(round(x2 * z2,1))
    case "/":
        print(round(x2 / z2,1))
    case _:
        print("Whut")
