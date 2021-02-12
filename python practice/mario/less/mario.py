from cs50 import get_int


while True:
    h = get_int("Height required beteen 1 and 8:\n")
    if(h > 0 and h <= 8):
        break;

for i in range(h):
    for j in range(h-(i+1)):
        print(" ", end = "")
    for n in range(i+1):
        print("#", end = "")
    print()

