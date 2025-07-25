# ========================================= #
# Extracting the digits from the number #
# ========================================= #

num1 = int(input("Enter the number to extract digits : "))

while num1 != 0:
    last_digit = num1 % 10
    print(last_digit)
    num1 //= 10

# ✅ This code extracts each digit from the right by taking modulo 10,
# then removes that digit by floor dividing the number by 10.
# 🕒 Time Complexity: O(log₁₀(N)) — because we're dividing by 10 in each iteration.


# ========================================= #
# Extracting the digits and counting them #
# ========================================= #

num2 = int(input("Enter the number to find length : "))
count = 0

if num2 == 0:
    count = 1
else:
    while num2 != 0:
        last_digit = num2 % 10
        print(last_digit)
        num2 //= 10
        count += 1

print("The length of number is : ", count)

# ✅ This version not only extracts digits but also counts them.
# It uses the same divide-by-10 approach while incrementing a counter for each digit.
# 🕒 Time Complexity: O(log₁₀(N)) — same logic, one extra operation (count++) per iteration.

# ========================================= #
# Counting them using Math Library #
# ========================================= #

from math import *

number = int(input("Enter the number to find length using Log : "))
def countDigits(number):
    return int(log10(number) + 1)
print("The length of number is ", countDigits(number))

# ✅ This uses logarithm base-10 to directly calculate the number of digits,
# as log₁₀(N) gives the number of digits minus 1.
# 🕒 Time Complexity: O(1) — Constant time, as it does one mathematical calculation.
# ================================================================================= #
# constantly dividig by any number leads to the time complexity as : O(log base dividing `number` * N)
# where dividing number is the base with which we are dividing it and N is the input size
# e.g if n = n / 5 then it will be as   =>  O ( log base 5 (N) )
