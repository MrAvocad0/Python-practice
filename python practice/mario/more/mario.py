from cs50 import get_int

# h is positive integer between 0 and 8 inclusive of 8

while True:
    h = get_int("Height required beteen 1 and 8:\n")
    if (h > 0 and h <= 8):
        break

# i = number of columns dictated by h
for i in range(h):
    # this prints spaces in terms of a upside down
    # right aligned pyramid
    for j in range(h - (i + 1)):
        print(" ", end = "")
    # this looks prints right sided pyramid
    # but with the spaces being printed before
    # we get a right aligned pyramid
    for n in range(i + 1):
        print("#", end = "")
    # follow with two spaces to create next left aligned pyramid
    print("  ", end = "")
    for k in range(i + 1):
        print("#", end ="")
    print()

