# Create the output function
def main():
    smiley = input("write something with an emoticon ").replace(":)", "🙂").replace(":(", "🙁")
    convert(smiley)


# Create our function convert: turns emoticons into emojis
def convert(face):
    print(face)

main()