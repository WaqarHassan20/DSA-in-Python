print("=================================")
print("Reversing an array using the loop")
print("=================================\n")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = arr.__len__()

print("Array : ",arr)

i = 0
j = length - 1

while(i < j):
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

print("Array : ", arr)

print("\n")
print("==================================")
print("Reversing an array using Recursion")
print("==================================\n")


arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length2 = arr2.__len__()

print("Array : ",arr2)

left = 0
right = length2 - 1

def reverse_array(m,n):
    if m < n:
        arr2[m], arr2[n] = arr2[n], arr2[m]
        reverse_array(m + 1, n - 1)

reverse_array(left, right)

print("Array : ", arr2)


print("\n")
print("======================================================")
print("Reversing an array using Recursion with inputs by user")
print("======================================================\n")

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length3 = arr3.__len__()
print(
    "The length of array is ", length3, ",So cannot give the ending value more than it"
)

start = int(input("Enter the starting value : "))
end = int(input("Enter the ending value : "))

print("Array : ",arr3)

l = 0
r = length3 - 1

def reverse_array(m,n):
    if m < n:
        arr3[m], arr3[n] = arr3[n], arr3[m]
        reverse_array(m + 1, n - 1)

reverse_array(start - 1, end - 1)

print("Array : ", arr3)


print("\n")
print("======================================================")
print("Reversing an array using Recursion with inputs by user")
print("======================================================\n")

myArr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(myArr3)
print("The length of array is", length, ", so cannot give the ending value more than it.")

start = int(input("Enter the starting position (1-based index): "))
end = int(input("Enter the ending position (1-based index): "))

# Validate input range
if start < 1 or end > length or start > end:
    print("Invalid range. Please enter values between 1 and", length, "with start <= end.")
else:
    print("Original Array:", myArr3)

    def reverse_array_fun(arr, start, end):
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            reverse_array_fun(arr, start + 1, end - 1)

    # Adjusting to 0-based indexing
    reverse_array_fun(myArr3, start - 1, end - 1)

    print("Reversed Array (from position", start, "to", end, "):", myArr3)


# 🔍 Time and Space Complexity Analysis 🧠
# All the provided code snippets aim to reverse an array (either fully or partially), and each one uses the same fundamental logic — swapping elements from both ends moving toward the center.

# ⏱ Time Complexity:
# For all versions — whether iterative or recursive — the time complexity is O(n), where n is the number of elements being reversed. Each element in the specified range is accessed and swapped exactly once.

# 🧮 Space Complexity:

# The iterative version (using a while loop) is the most efficient, requiring only O(1) extra space 🧊 since all swaps happen in-place.

# The recursive versions (with or without user input) require O(n) space 🧠 due to the function call stack — each recursive call adds a new layer, leading to linear growth.

# 🎯 Input Handling:
# The last two snippets add user input and validation, enhancing usability 🧑‍💻, but this logic doesn't impact the core time or space complexity.
