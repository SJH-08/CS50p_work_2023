# Ask user's input (str)
def main():
    text = input("Input: ")
    remove_vowel(text)


# Define vowel range
def remove_vowel(string):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    char = []
# Remove vowels
    for twitter in string:
        if twitter in vowels:
            char.append("")
        else:
            char.append(twitter)
    char = "".join(char)

    print(char)

main()

