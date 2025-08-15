print("=====================================")
print("Printing 1 to N using Tail Recursion")
print("=====================================")

def one_to_N_Tail(value,count):
    if value > count:
        return
    else:
        print(value)
        one_to_N_Tail(value + 1, count)

one_to_N_Tail(1,5)


print("=====================================")
print("Printing 1 to N using Head Recursion")
print("=====================================")

def one_to_N_Head(value):
    if value== 0:
        return
    else:
        one_to_N_Head(value - 1)
        print(value)

one_to_N_Head(5)


print("=====================================")
print("Printing N to 1 using Head Recursion")
print("=====================================")

def n_to_One_Head(value,count):
    if value > count:
        return
    else:
        n_to_One_Head(value + 1, count)
        print(value)

n_to_One_Head(1, 5)


print("=====================================")
print("Printing N to 1 using Tail Recursion")
print("=====================================")

def n_to_One_Tail(value):
    if value == 0:
        return
    else:
        print(value)
        n_to_One_Tail(value - 1)

n_to_One_Tail(5)


# ⏱ Time and 🧠 Space Complexity (All Snippets):
# All the recursion functions across your code snippets perform one recursive call per function invocation, and they run for n levels (whether counting up or down). Therefore, the time complexity for each function is O(n). Regarding space complexity, although some functions are written using tail recursion, Python does not support tail call optimization, so each recursive call adds a new frame to the call stack. Thus, the space complexity is also O(n) in all cases.
