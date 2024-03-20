# Import library to use
import sys
from tabulate import tabulate
import csv

# Arg = 1 (name of an existing python file or path)
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
# File does not end with ".csv"
else:
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a csv file")

# Empty variable to store the output
menu = []

# Input 1 CLA
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)


# Output ASCII art format
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


# File does not exist
except FileNotFoundError:
    sys.exit("File does not exist")
