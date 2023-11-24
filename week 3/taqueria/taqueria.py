menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
#Induce infinite loop --> break only when user provides right input
total = 0
while True:
# 1 item per line
# Prompt the user for items from the dict menu
# Assume prompt is titlecase
# Check item is in the menu
# Print the total 2 dec $
    try:
        prompt = input("Item: ")
        item = prompt.title()
        total += menu[item]
        print(f"Total: ${total:.2f}")
# ctrl d: ends the input + print new line
    except EOFError:
        print("\n")
        break
#catch key error if item not in the menu
    except KeyError:
        pass

