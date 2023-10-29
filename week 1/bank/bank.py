# Ask for user's input
# Remove any extra space
# Convert into lowercase
greet = input("Greeting: ").strip().lower()

# Define If else statement
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h") and greet != "hello":
    print("$20")
else:
    print("$100")
