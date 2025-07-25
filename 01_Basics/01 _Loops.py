for row in range(1,10):
    for col in range(1,10):
        print("*", end=" ")
    print()

# This code prints a 9x9 grid of stars using nested loops. The outer loop runs from 1 to 9 and controls the number of rows, while the inner loop also runs from 1 to 9 and prints stars in each row. The print("*", end=" ") statement prints stars on the same line with spaces, and after completing each row, print() moves the cursor to the next line. Since the inner loop runs 9 times for each of the 9 outer loop iterations, the total number of operations is 9 × 9 = 81. Therefore, the time complexity of this code is O(n²), where n is the number of rows or columns.
