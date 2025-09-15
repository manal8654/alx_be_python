# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw square pattern using while + for
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # new line after each row
    row += 1
