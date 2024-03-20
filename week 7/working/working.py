#Import library to use
import re
import sys

#Prompt user for input(str)
def main():
    print(convert(input("Hours: ")))


#Input in 12h format
#AM and PM capitalized
#Space between number and AM/PM
#Nightshift possible
def convert(s):
    matches = re.fullmatch(r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)", s)
    if matches:
#minutes optional
        start_minutes = 0
        end_minutes = 0
#Check the hour format
        start_hour = check_hour(int(matches.group(1)), matches.group(3))
        end_hour = check_hour(int(matches.group(4)), matches.group(6))
#If minutes, check the format
        if matches.group(2):
            start_minutes = check_minute(int(matches.group(2)))
        if matches.group(5):
            end_minutes = check_minute(int(matches.group(5)))
#Return Output in 24h format
        return f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"
#Raise ValueError if format invalid or time invalid
    else:
        raise ValueError

#Check 0 < h <= 12
def check_hour(hour, format):
#Raise ValueError if format invalid or time invalid
    if hour == 0 or hour > 12:
        raise ValueError
#Midnight
    if hour == 12 and format == "AM":
        return 0
#Morning
    elif format == "AM":
        return hour
    #Lunch
    elif hour == 12 and format == "PM":
        return hour
#Afternoon
    else:
        return hour + 12


#Check 0 < m < 60
def check_minute(minutes):
    if minutes > 59:
        raise ValueError
    return minutes


if __name__ == "__main__":
    main()
