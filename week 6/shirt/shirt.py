# Import library to use
import sys
import os
from PIL import Image, ImageOps

def main():
    check_input()
    check_extension()
    overlay_image()

def check_input():
# Arg = 2 (name of an existing python file or path)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


#Separate file extension from name of file 
# File does not end with ".jpeg", ".png", ".jpg"
#Input file extension != Output file extension
def check_extension():
    ext = [".jpeg", ".png", ".jpg"]
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    if ext1[1] not in ext:
        sys.exit("Invalid input")
    elif ext2[1] not in ext:
        sys.exit("Invalid ouput")
    elif ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")


def overlay_image():
# Open the shirt (image to overlay)
# Open the input image
# Get its size + Resize and crop it
# Overlay an image on top
# Save the result in new file
    try:
        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])
        muppet = ImageOps.fit(muppet, shirt.size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])

# File does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
