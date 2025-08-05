# =============================================================== #
#  How hasing works to count the entries of digit in other array  #
# =============================================================== #

# List of numbers where we want to count occurrences
n = [1, 3, 5, 7, 8, 9, 4, 2, 6, 10, 4, 5, 6, 7, 3, 3, 6, 7, 3]

# Numbers to check how many times they occurred in n
m = [10, 1, 111, 9, 5, 67, 2, 3, 6, 7, 4, 5] 

# # Step 1: Create a hash list to count occurrences (0 to 111 to safely handle large numbers)
# max_val = max(max(n), max(m))  # Maximum value we might encounter
# hash_list = [0] * (max_val + 1)  # Initialize count list

num_hash_list = [0] * 11  # Initialize count list


# Step 2: Count occurrences from list n
for num in n:
    num_hash_list[num] += 1

# Step 3: Print each number in m with how many times it occurred in n
print("---------------")
print("Number | Count")
print("---------------")
for num in m:
    if num < 0 or num >= len(num_hash_list):
        print(f"{num:>6} | {0}")
    else:
        print(f"{num:>6} | {num_hash_list[num]}")

# this >6 is used for the formatting the number and count in two different equal columns to show values with count
# Same counting of digits have done before but using the dictionary concept in python

# ------------------------------------------------------------
# Time and Space Complexity Analysis:
#
# Time Complexity:
# The code performs three main tasks:
#   1. It finds the maximum value in lists `n` and `m`, which takes O(N + M) time.
#   2. It iterates over the list `n` to count occurrences, which takes O(N) time.
#   3. It then iterates over the list `m` to print the count of each number, which takes O(M) time.
# Therefore, the overall time complexity is O(N + M).
#
# Space Complexity:
# The code creates an auxiliary list called `hash_list` of size K + 1,
# where K is the maximum value present in either list `n` or `m`.
# This is used to store the count of each number. Hence, the space complexity is O(K).
# The input lists `n` and `m` take O(N) and O(M) space respectively, but since they are inputs,
# they are not considered part of the extra space complexity.
# ------------------------------------------------------------


# =============================================================== #
#     How hasing works to count the characters in other array     #
# =============================================================== #


# List of char where we want to count occurrences
x = "azyxxayyzacdefaaa"

# char to check how many times they occurred in x
y = ['x','y','a','z','c','d','e','f'] 

char_hash_list = [0] * 27

for char in x:
    ascii_value = ord(char)
    index = ascii_value - 97
    char_hash_list[index] += 1

print("---------------")
print("Char | Count")
print("---------------")

for char in y:
    ascii_value = ord(char)
    index = ascii_value - 97
    print(f"{char:>6} | {char_hash_list[index]}")

# ------------------------------------------------------------
# Time and Space Complexity Analysis:
#
# Time Complexity:
# The program performs two main loops:
#   1. It iterates over the characters in the input string `x` to count their frequency. 
#      This loop runs in O(N), where N is the total number of characters in the string.
#   2. It then iterates over the list `y` to print the count of each character, which runs in O(M),
#      where M is the number of query characters.
# Therefore, the overall time complexity is O(N + M).
#
# Space Complexity:
# The space used for `char_hash_list` is fixed at 26 (or 27 in your code),
# representing lowercase English letters ('a' to 'z'), so the space complexity is O(1) constant.
# The input lists `x` and `y` use O(N) and O(M) space respectively, but as inputs,
# they are not counted as extra space.
# ------------------------------------------------------------
