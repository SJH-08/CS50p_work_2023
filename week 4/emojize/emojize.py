# import the library to use
import emoji

# Prompt user for an emoji (str)
prompt = input("Input: ")

# Output the emoji version
# (provide alias)
# str outside the emoji method
print("Output: ", emoji.emojize(prompt, language="alias"))
