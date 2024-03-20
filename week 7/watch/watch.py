#Import library to use
import re
import sys


#Prompt user for input (str)
#Remove extra space
def main():
    print(parse(input("HTML: ")))



def parse(s):
#Capture the src inside the iframe
    if re.search(r"<iframe (.+)></iframe>", s):
#Define the YT URL: http(s), (www)
        if matches := re.search(r"https?://(?:www.)?youtube\.com/embed/([a-z_A-Z_0-9]+)", s, re.IGNORECASE):
#If match: return a cleaner version
            return "https://youtu.be/" + matches.group(1)
#Otherwise return None
        else:
            return None


if __name__ == "__main__":
    main()
