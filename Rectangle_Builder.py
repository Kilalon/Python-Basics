length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
symbol = input("Enter the symbol you would like")

for x in range(width):
    for y in range(length):
        print(symbol, end="")
    print()