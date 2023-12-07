# Import library to use
import inflect

p = inflect.engine()

# Induce infinite loop until user cooperates
# Assume the user will input at least one name
# Create empty list

names = []
while True:
# Prompt user for names
# 1 name per line
# Store input in the list
    try:
        prompt = input("Name: ")
        names.append(prompt)
# Separator: (n-1)(,) and at the end
        output = p.join((names))


# ctrl d --> exit program
    except EOFError:
        print("\n")
        break

# Print the output
print("Adieu, adieu, to", output)
