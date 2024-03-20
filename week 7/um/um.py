#Import the library to use
import re
import sys


#Prompt the user for input (str)
#Output the number of "um" (int)
def main():
    print(count(input("Text: ")))

#Case insensitive
#Count the number of "um" as word
#Define bounderies
def count(s):
    um = 0

    um += len(re.findall(r"\bw?(um)\W?\b", s, re.IGNORECASE))

    return um

if __name__ == "__main__":
    main()
