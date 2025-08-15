print("====================")
print("First function start ")
print("====================")

def print_x_times(value,count):
    print(value)
    if count != 0:
        print_x_times(value, count - 1)

print_x_times(10, 5)

print("=====================")
print("A new function Starts")
print("=====================")

def print_fun(value,count):
    if count == 0:
        return
    print(value)
    print_fun(value, count - 1)

print_fun(15, 5)

print("=====================")
print("A new function Starts")
print("=====================")

def print_loop(value,condition):
    if value>condition:
        return
    else:
        print(value)
        print_loop(value + 1, condition)

print_loop(1, 10)


# The above example is an example of tail recursion ✅
# ✅ Why is it tail recursion?
# The last statement executed in the function is the recursive call:
# print_loop(value + 1, condition)
# No operation is performed after the recursive call returns.
# So it's a tail call.

# ================================== #
# Time and Space complexity of code 
# ================================== #

# Time and Space Complexity Analysis:
# All three functions—print_x_times(value, count), print_fun(value, count), and print_loop(value, condition)—perform a recursive call that executes n times based on the count or condition. Therefore, each function has a time complexity of O(n). Regarding space complexity, all three exhibit tail recursion (the recursive call is the last operation in the function), making them eligible for O(1) space in languages or interpreters that support tail call optimization. However, in Python, which does not optimize tail calls, each function will still consume a new stack frame per call, so the space complexity remains O(n) in practice.

