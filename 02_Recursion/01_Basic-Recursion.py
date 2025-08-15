# Basic non parameterized function calls in recursion

print("=====================")
print("Non paramed function")
print("=====================")

count = 0

def print_name():
    global count
    if count==5:
        return
    print("My name is Waqar")
    count += 1
    print_name()  # This is called as Tail Recursion as there is no job to done after call

print_name()

print("=====================")
print("A new function Starts")
print("=====================")

count2 = 0

def print_name2():
    global count2
    if count2==5:
        return
    count2 += 1
    print_name2()  # This is called as Head Recursion as their is some job to done after the call
    print("What is your name ?")

print_name2()


# Time and Space Complexity Analysis:
# Both print_name() (tail recursion) and print_name2() (head recursion) execute the recursive call five times, making their time complexity O(n), where n = 5 in this case. However, the space complexity differs due to the order of operations. In print_name(), the recursive call is the last operation (tail recursion), so theoretically, a compiler or interpreter that supports tail call optimization could reuse stack frames, resulting in O(1) space complexity. On the other hand, print_name2() performs operations after the recursive call (head recursion), so each call must wait for the next one to complete, resulting in O(n) space complexity due to stack frame buildup.
