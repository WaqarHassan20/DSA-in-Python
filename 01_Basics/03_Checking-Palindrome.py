# ========================================= #
# Checking a number is palindrome or not #
# ========================================= #

input_Number = int(input("Enter the number to check palindrome : "))

def check_palindrome(n):
    number = n
    reversed_number = 0
    last_digit =  0
    while n != 0:
        last_digit = n % 10
        reversed_number = (reversed_number * 10) + last_digit
        n //= 10
    if reversed_number == number:
        return True
    else:
        return False

if check_palindrome(input_Number):
    print("Yes, the number is palindrome")
else:
    print("No, the number is not palindrome")


# 🧠 Working Logic:
# This program checks whether a given number is a palindrome (i.e., it reads the same backward as forward). The user inputs a number, which is passed to the check_palindrome function. Inside this function, the number is reversed by extracting its last digit using modulo (% 10), appending it to a new number (reversed_number), and then removing the last digit using integer division (// 10). This process continues until the original number becomes 0. After the loop, the reversed number is compared to the original number to determine if it’s a palindrome.


# ⏱️ Time Complexity:
# O(d), where d is the number of digits in the input number.

# Because each digit is processed once during the reversal.

# 🧠 Space Complexity:
# O(1) constant space.

# Only a few variables are used (number, reversed_number, last_digit), and no additional data structures or recursion.
