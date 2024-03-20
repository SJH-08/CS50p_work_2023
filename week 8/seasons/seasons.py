#Import library to use
from datetime import date
import sys
import inflect


def main():
#Prompt user for DOB (YYYY-MM-DD)
    print(get_dob(input("Date of Birth: ")))


def get_dob(s):
#Convert str in valid date format
    try:
        dob = date.fromisoformat(s)
#Exit the program if invalid format
    except ValueError:
        sys.exit("Invalid date")

#Assume user was born at midnight
#Assume today is also midnight
#Calculate difference of days
#Convert diff days in min
    min = (date.today() - dob).days * 24 * 60

#Convert min (int) in words
#Output age in minutes to the nearest int
#No and
#Capitalized
    p = inflect.engine()

    return f'{p.number_to_words(min, andword="").capitalize()} minutes'


if __name__ == "__main__":
    main()
