#Import library to use
from validator_collection import validators, errors

#Prompt user for input (str)
def main():
    print(validate(input("What's your email address? ").strip()))


def validate(s):
#Use the validator to check the input
    try:
        email = validators.email(s)
#Return Invalid if address invalid
    except errors.InvalidEmailError as error:
        return "Invalid"
    except ValueError as error:
        return "Invalid"
#Return Valid if address valid
    else:
        return "Valid"


if __name__ == "__main__":
    main()
