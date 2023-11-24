# Store month in a list
list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Induce infinite loop --> break only when user provides right input
while True:
    date = input("Date: ")
    try:
# Prompt user for a date (MM/DD/YYYY)
# Split the input on "/"
#Assume a month = 31 D
# Output (YYYY-MM-DD)
# 2 zeros padding
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
# Prompt user for a date (month, D, YYYY)
# Split the input on "," and " "
#Check the month is in the list
#Assume a month = 31 D
# Output (YYYY-MM-DD)
# 2 zeros padding
        else:
            if "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                day = int(day)
                year = int(year)
                month = list.index(month) + 1
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
# Catch Value and Index errors
    except (ValueError, IndexError):
        pass
