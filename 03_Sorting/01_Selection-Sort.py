array = [8, 7, 2, 5, 4, 6, 3, 9, 1]

print("Simple Array : ", array)
def selectionSort_Ascending(arr):
    length = len(arr)
    for i in range(0,length):
        minimum_index = i
        for j in range(i+1,length):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

selectionSort_Ascending(array)
print("Ascending Array : ", array)


def selectionSort_Descending(arr):
    length = len(arr)
    for i in range(0,length):
        maximum_index = i
        for j in range(i+1, length):
            if arr[j] > arr[maximum_index]:
                maximum_index = j
        arr[i], arr[maximum_index] = arr[maximum_index], arr[i]

selectionSort_Descending(array)
print("Descending Array : ", array)


# This Python script 🐍 demonstrates the Selection Sort algorithm to sort an array in both ascending 🔼 and descending 🔽 order. Selection Sort is a simple sorting technique that divides the array into two parts: a sorted part ✅ and an unsorted part 🔄. At each step, it finds the smallest (or largest) element from the unsorted part and places it at the correct position by swapping it.

# The algorithm uses two loops 🔁🔁 — the outer loop selects the position to fill, and the inner loop finds the minimum (or maximum) element. This leads to a time complexity of O(n²) ⏱️, because it always performs the same number of comparisons, even if the array is already sorted.

# Since it doesn’t use any extra memory and swaps elements directly in the original array, the space complexity is O(1) 💾. While Selection Sort is easy to understand and implement 🧠, it’s not efficient for large datasets 📊 compared to faster algorithms like Merge Sort or Quick Sort ⚡.
