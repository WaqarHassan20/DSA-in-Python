inputNum = int(input("Enter the number to find fibnocci value : "))
def fibnocci_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnocci_function(n - 1) + fibnocci_function(n - 2)

res = fibnocci_function(inputNum)

print("Fibnocci of", inputNum, "is : ", res)

# =============================================================== #

inputNum = int(input("Enter the number to find fibnocci value : "))
sum = 0

def fib_by_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a,b = 0,1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b

result = fib_by_loop(inputNum)

print("Fibnocci of", inputNum, "is : ", result)
