# ============================================================================================== #
#  Finding the factors by taking the modulos opeartor and reaminder checking and appending
# ============================================================================================== #

input_Number = int(input("Enter the number to print factors by full loop : "))

def print_factors(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

# print_factors(input_Number)
all_factors = print_factors(input_Number)
print("Factors of", input_Number, "are : ")
for fact in all_factors:
    print(fact)


# 🧠 Working Logic:
# This brute-force method checks every number from 1 to n. If the number divides n completely (remainder is 0), it is a factor and is added to the list.

# ⏱️ Time Complexity:
# O(n): The loop runs from 1 to n.

# 🧠 Space Complexity:
# O(k): Where k is the number of factors (usually less than n), stored in a list.


# ============================================================================================== #
#  Slightly better approach for finding the factors by reducing the for loop to half of the number
# ============================================================================================== #

input_Number2 = int(input("Enter the number to print factors by half loop : "))

def print_factors2(n):
    factors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors

# print_factors(input_Number)
all_factors2 = print_factors2(input_Number2)
print("Factors of", input_Number2, "are : ")
for fact in all_factors2:
    print(fact)


# 🧠 Working Logic:
# Instead of checking all the way to n, it only checks up to n/2, since no number greater than n/2 (except n itself) can divide n. Finally, it adds n as a factor manually.

# ⏱️ Time Complexity:
# O(n/2) = O(n): Still linear but slightly faster than the full loop.

# 🧠 Space Complexity:
# O(k): Same as before — number of factors stored.

# ============================================================================================== #
#  Optimal approach for finding the factors by traversing only to the limit got by taking sqaure root of number
# ============================================================================================== #

from math import sqrt
input_Number3 = int(input("Enter the number to print factors by square root method : "))

def print_factors3(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    return factors

all_factors3 = print_factors3(input_Number3)
all_factors3.sort()
print("Factors of", input_Number3, "are : ")
for fact in all_factors3:
    print(fact)

#     🧠 Working Logic:
# This method leverages the fact that factors appear in pairs:

# If i divides n, then n/i is also a factor.

# So, it only checks up to √n, and for every factor found, it adds both i and n//i, avoiding duplicates.

# ⏱️ Time Complexity:
# O(√n) — Significantly more efficient for large numbers.

# 🧠 Space Complexity:
# O(k) — Number of factors collected, but the loop itself uses constant space.
