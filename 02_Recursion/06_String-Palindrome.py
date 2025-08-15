print("==============================")
print("Checking palindrome using Loop")
print("==============================\n")

original = input("Enter the input string : ")

start = 0
end = len(original) - 1

def string_palindrome(original, start, end):
    while start < end:
        if original[start] != original[end]:
            return False
        else:
            start += 1
            end -= 1
        return True
res = string_palindrome(original, start, end)

if res == True:
    print("This string", original.upper(), "is palindrome")
else:
    print("This string", original.upper(), "is NOT palindrome")

# Time Complexity: O(n)
# The loop compares characters from the beginning and end, moving toward the center. In the worst case, it compares each character once, making it linear with respect to the string length.

# Space Complexity: O(1)
# No extra space is used — only a few integer variables for indexing, so the memory usage remains constant.


print("\n")
print("=====================================")
print("This was my logic by reversing string")
print("=====================================\n")

original2 = input("Enter the input string : ")
to_reverse2 = list(original2)

start2 = 0
end2 = len(to_reverse2) - 1

def reverse_function(str,start,end):
    if start > end:
        return
    to_reverse2[start], to_reverse2[end] = to_reverse2[end], to_reverse2[start]
    reverse_function(str, start + 1, end - 1)

reverse_function(original2, start2, end2)

reversed_str2 = ''.join(to_reverse2)

print(original2)
print(reversed_str2)

if reversed_str2 == original2:
    print("This string is palindrome")
else:
    print("This string is not palindrome")

# Time Complexity: O(n)
# The recursion performs n/2 swaps and visits each pair once, so the runtime is linear.

# Space Complexity: O(n)
# Since recursion is used, each call adds a new frame to the call stack. Therefore, the space complexity grows linearly with the input size.


print("\n")
print("===================================")
print("Checking palindrome using Recursion")
print("===================================\n")

inputStr = input("Enter the input string : ")

s = 0
e = len(inputStr) - 1

def reverse_function2(str,start,end):
    if start >= end:
        return True
    if str[start] != str[end]:
        return False
    return reverse_function2(str, start + 1, end - 1)

result = reverse_function2(inputStr, s, e)

if result == True:
    print("The string", inputStr.upper(), "is palindrome")
else:
    print("The string", inputStr.upper(), "is NOT palindrome")

# Time Complexity: O(n)
# Each character pair is checked once from both ends, so it's linear with the string size.

# Space Complexity: O(n)
# Again, recursive calls consume stack space. For a string of length n, about n/2 recursive calls are made.
