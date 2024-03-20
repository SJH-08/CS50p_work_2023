# Import library to use
import sys

# Arg = 1 (name of an existing python file or path)
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
# File does not end with ".py"
else:
    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

# Empty variable to store the output
loc = 0

try:

# Open and read each lines of the file
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

# Does not count comments "#" or full blank lines or whitespaces
# Also consider comments on the same line as code
        for line in lines:
            if line == "\n" or line.strip().startswith("#") or len(line.strip()) < 1:
                pass
            else:
                loc += 1
# Output: nb of lines of code in the file
        print(loc)

# File does not exist
except FileNotFoundError:
    sys.exit("File does not exist")
