# Ask user's input (camelCase)
def main():
    user = input("camelCase: ")
    print("snake_case: ", end="")
    convert(user)

# Convert camelCase into snake_case
# Insert _
# lowercase
def convert(string):
    snake = ""
    for camel in string:
        if camel.isupper():
            snake += "".join("_" + camel.lower())
        else:
            snake += "".join(camel)
    print(snake)

main()
