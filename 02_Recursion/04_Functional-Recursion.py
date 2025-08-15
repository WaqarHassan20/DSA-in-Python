# print("=========================================")
# print("Printing sum of natural nums by Recursion")
# print("=========================================")

# def sum_N(sum,iterator,limit):
#     if iterator > limit:
#         print("Sum of N numbers is : ", sum)
#         return

#     sum_N(sum + iterator, iterator + 1, limit)

# sum_N(0, 1, 5)

# print("============================================")
# print("Printing sum of N nums by returning function")
# print("============================================")


# def sumByBackTracking(num):
#     if num == 1 :
#         return 1
#     return num + sumByBackTracking(num - 1)

# inputNum = int(input("Enter the value of n : "))
# sum = sumByBackTracking(inputNum)
# print("Sum from 1 to", inputNum, "is : ", sum)


# # ⏱ Time and 🧠 Space Complexity:
# # Both sum_N(sum, iterator, limit) and sumByBackTracking(num) perform one recursive call per level, and process from 1 to n, so they both have time complexity O(n).

# # For sum_N(...), although it is written in a tail-recursive style, Python does not optimize tail calls, so it still uses O(n) stack space.

# # For sumByBackTracking(...), it is non-tail (head) recursion with computation after the recursive call, so it also uses O(n) space.

# # 👉 Therefore, for both functions:
# # ✅ Time Complexity: O(n)
# # ✅ Space Complexity: O(n)


print("============================================")
print("Printing factorial of number using recursion")
print("============================================")

def factorial(num):
    if num == 0 or num == 1 :
        return 1
    return num * factorial(num - 1)
inputNum2 = int(input("Enter the number to find factorial : "))
fact = factorial(inputNum2)
print("Factorial of ", inputNum2, "is ", fact)


# ✅ Time Complexity: O(n)
# The function calls itself once for each number from n down to 1.

# So it performs n recursive calls and n - 1 multiplications.

# ✅ Space Complexity: O(n)
# Each recursive call is added to the call stack.

# Since Python does not support tail call optimization, the stack grows up to n frames.

# Conclusion:
# For the input n, the recursive factorial function has:
# 🔹 Time Complexity: O(n)
# 🔹 Space Complexity: O(n)
