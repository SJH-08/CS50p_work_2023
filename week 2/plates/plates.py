# Ask user's input (assume uppercase)
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define conditions of validity
def is_valid(s):
    length = len(s)

# Must start with at least 2 letters
    if s[0:1].isdecimal() == True:
        return (False)

# May contain 2 <= x <= 6 chars
    elif len(s) < 2 or len(s) > 6:
        return(False)
# no special characters --> not a letter, not a nb
# no space
    elif s[0:5].isalnum() == False:
        return (False)

# Get the length of the string for negative indexing --> only digits remaining
# AAA222 ok
# AAA22A no
    for i in range(len(s)-1):
        if s[i].isdecimal() == True and s[i+1].isalpha() == True:
            return (False)
# 1st nb used cannot be a 0
        for j in range(len(s)-1):
            if s[j] == "0" and s[j+1].isdigit():
                return (False)

    else:
        return (True)

main()
