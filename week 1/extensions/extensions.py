# Ask for user's input
# Remove any extra space
# Convert into lowercase
mime = input("File name: ").strip().lower()

# Define If else statement image, application,text
if mime.endswith(".gif"):
    print("image/gif")
elif mime.endswith(".jpg") or mime.endswith(".jpeg"):
    print("image/jpeg")
elif mime.endswith(".png"):
    print("image/png")
elif mime.endswith(".pdf"):
    print("application/pdf")
elif mime.endswith(".zip"):
    print("application/zip")
elif mime.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
