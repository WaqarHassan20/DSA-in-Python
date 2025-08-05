# ============================================================================================== #
#  Finding the frequency of the each number in the dictionary to tell how many time it occurs
# ============================================================================================== #

print("=========================================")
print("Finding frequency by using if else logic")
print("=========================================")

nums = [1, 3, 2, 4, 7, 7, 5, 3, 2, 5, 4, 5, 4, 3]
freq_map = dict()

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

for key, value in freq_map.items():
    print("Frequency of ", key, "is", value)


# 🧠 Working Logic:
# This program calculates the frequency (count) of each unique number in the given list nums. It uses a dictionary freq_map to store each number as a key and its frequency as the value. The program iterates over the list using a for loop. For each element, it checks whether the number is already in the dictionary:

# If it exists, it increments the count by 1.

# If not, it adds the number to the dictionary with a count of 1.

# After building the frequency map, it loops through the dictionary using .items() and prints the frequency of each number.


# ⏱️ Time Complexity:
# Loop over n elements in nums → O(n)

# Dictionary operations (in, get, set) are O(1) on average.

# Final loop over unique elements (let’s say k items) → O(k)

# Total Time Complexity → O(n + k) ≈ O(n)

# 🧠 Space Complexity:
# The dictionary freq_map stores up to k unique elements from the list.

# Space Complexity → O(k)
# Where k is the number of unique numbers in the input list.


# ============================================================================================== #
#  Finding the frequency of the each number in the dictionary by using the get() function
# ============================================================================================== #

print("=========================================")
print("Finding frequency by using get() function")
print("=========================================")
nums2 = [1, 3, 2, 4, 7, 7, 5, 3, 2, 5, 4, 5, 4, 3, 3, 4, 5, 6, 7, 7, 8, 8, 9]
hash_map = dict()

for i in range(0, len(nums2)):
    hash_map[nums2[i]] = hash_map.get(nums2[i], 0) + 1

for key, value in hash_map.items():
    print("Frequency of ", key, "is", value)
