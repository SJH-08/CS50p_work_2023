# Ask for user's input
def main():
    greet = input("Greeting: ")
    print("$", value(greet), sep="")

# Define bounderies
def value(greeting):
# Remove any extra space
# Convert into lowercase
    sentence = greeting.strip().lower()

# Hello starter = 0
    if sentence.startswith("hello"):
        return 0
# H starter = 20
    elif sentence.startswith("h") and sentence != "hello":
        return 20
    else:
# other = 100
        return 100

if __name__ == "__main__":
    main()
