# store in a dict
#Induce infinite loop --> break only when user provides right input
grocery = {}
while True:
# Prompt user for items
# 1 item per line
# case insensitive
    try:
        item = input().lower()
        grocery[item] = grocery.get(item, 0) + 1

# Break when input ctrl d EOFError
# Output list in uppercase alphabetically with nb of occurence
    except EOFError:
            print("\n")
            for key in sorted(grocery.keys()):
                print(grocery[key], key.upper())
            break
    
# Catch KeyError
    except KeyError:
            pass

