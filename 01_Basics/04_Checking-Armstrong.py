import math

input_Number = int(input("Enter the number to check Armstrong : "))

def count_length(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def check_armstrong(n):    
    number_of_digits = count_length(n)
    number = n
    result = 0
    
    while n != 0:
        last_digit = n % 10
        result += math.pow(last_digit, number_of_digits)
        n //= 10
        
    if result == number:
        return True
    else:
        return False


if (check_armstrong(input_Number)):
    print("Yes, the number is Armstrong number")
else:
    print("No, the number is not Armstrong number")


# 🧠 Working Logic:
# This program checks if a number is an Armstrong number (also known as a narcissistic number). An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because:
# 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

# The program first takes an integer input and calculates the total number of digits using the count_length() function. Then, in check_armstrong(), it processes each digit by:

# Extracting it using % 10,

# Raising it to the power of the number of digits,

# Adding it to the result,

# Removing the digit using // 10.

# After processing all digits, it compares the result with the original number. If they match, it's an Armstrong number.


# ⏱️ Time Complexity:
# Let d = number of digits in the number.

# count_length(n):

# Processes each digit once → O(d)

# check_armstrong(n):

# Also loops through each digit → O(d)

# Each digit undergoes a power operation using math.pow() which takes O(log k) time, where k is the exponent (number of digits), but since k is small (max ~10), we treat it as constant.

# Total Time Complexity:
# 🔸 O(d)




# 🧠 Space Complexity:
# No recursion or data structures used.

# Only variables (number, result, last_digit, etc.)

# Total Space Complexity:
# 🔸 O(1) (constant space)

