from cs50 import get_string

# Get name using get_string from cs50 library
answer = get_string("What is your name?\n")

# if no name given print Hello, World.
# if name given print hello name.
if answer == "":
    print("Hello, world!")
else:
    print("Hello,", answer)
