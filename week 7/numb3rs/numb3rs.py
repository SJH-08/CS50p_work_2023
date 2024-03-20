#Import libary to use
import re
import sys

#Prompt user input (str)
#Remove extra space
def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
#.#.#.# format --> unites, dizaines, centaines
# 0 <= n <= 255
    pattern = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"

    if re.search(fr"^{pattern}\.{pattern}\.{pattern}\.{pattern}$", ip, re.IGNORECASE):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
