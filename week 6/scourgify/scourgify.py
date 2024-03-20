# Import library to use
import sys
import csv

# Arg = 1 (name of an existing python file or path)
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
# File does not end with ".csv"
else:
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Could not read", sys.argv[1])


try:
# Empty variable to store the output
    list = []
# Read name and house
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)

# Split variables on the ","
# Remove spaces
        for row in reader:
            name = row["name"]
            last, first = name.split(",")
            first = first.strip()
            last = last.strip()
            house = row["house"]
# Create dict
# Append on the empty list
            list.append({"first": first, "last": last, "house": house})


# File does not exist
except FileNotFoundError:
    sys.exit("File does not exist")

# Create new file
# Write headers first last house
# Get the data from the previous file
with open(sys.argv[2], "w") as file2:
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in list:
        writer.writerow({"first": student["first"], "last":student["last"], "house": student["house"]})




