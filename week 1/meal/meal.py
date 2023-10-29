# Ask user's input (str)
def main():
    meal = input("What time is it? ")

# Call convert()
# Define the meal times
    if 7.0 <= convert(meal) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(meal) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(meal) <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
# Split the input into 2 variables (str)
    hours, minutes = time.split(":")
# Convert str into float
    h = float(hours)
    m = float(minutes)/60
    converted = h + m
    return converted

if __name__ == "__main__":
    main()
