# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns (printing asterisks)
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to the next line after finishing a row
    row += 1
