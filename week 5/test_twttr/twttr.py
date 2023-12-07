# Ask user's input (str)
def main():
    text = input("Input: ")
    print(shorten(text))


# Define vowel range
# Create empty list
def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    char = []
# Remove vowels: isolate them
    for twitter in word:
        if twitter in vowels:
# Add the empty list + nothing
            char.append("")
        else:
# Add empty list + found vowels
            char.append(twitter)
# Join nothing + list
    char = "".join(char)

    return char

if __name__ == "__main__":
    main()

