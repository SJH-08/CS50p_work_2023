# Ask for user's input
# Remove any extra space
# Convert into lowercase
def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip(" ").lower()
    answer(x)

# Define the answer function
def answer(n):
    if n == "42":
        print("Yes")
    elif n == "forty-two":
        print("Yes")
    elif n == "forty two":
        print("Yes")
    else:
        print("No")

main()
