array = [8, 7, 2, 5, 4, 6, 3, 9, 1]
length = len(array)

print("Unsorted Array : ", array)

def Bubble_Sort_Ascending(array):
    for i in range(0,length-1):
        for j in range(0, length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]

Bubble_Sort_Ascending(array)
print("Ascending Array Sort : ", array)

def Bubble_Sort_Descending(array):
    for i in range(0,length-1):
        for j in range(0, length - i - 1):
            if array[j] < array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]


Bubble_Sort_Descending(array)
print("Descending Bubble Sort : ", array)


# Optimized version of code using a check flag

array2 = [8, 7, 2, 5, 4, 6, 3, 9, 1]
# array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(array2)

def Optimized_Bubble_Sort(array):
    flag = True
    for i in range(0, length-1):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        if flag == True:
            break
Optimized_Bubble_Sort(array2)
print("Optimized Bubble Sort : ", array2)

# The Bubble_Sort_Ascending function sorts a list in ascending order using the Bubble Sort algorithm. First, it calculates the length of the array using len(array). The outer loop runs from index 0 to length - 2, representing each pass through the array. With each pass, the largest unsorted element "bubbles up" to its correct position at the end. The inner loop runs from 0 to length - i - 1, comparing adjacent elements. If the current element is greater than the next one, they are swapped using Python’s multiple assignment syntax. This comparison and swap continue until all elements are in order. The length - i - 1 part ensures that already sorted elements at the end of the list are skipped in future passes. This process continues until the array is fully sorted. The logic is simple but effective for small datasets and demonstrates the core idea of comparison-based sorting.


# Time and Space Compexity of this sorting code

# The time complexity of the Bubble_Sort_Ascending function is O(n²) in the best, average, and worst cases because it uses two nested loops to compare and swap adjacent elements. Even if the array is already sorted, the function still performs all the comparisons since there is no early exit optimization implemented. This makes Bubble Sort inefficient for large datasets. However, its logic is simple and easy to understand, which makes it a good choice for learning purposes. The space complexity is O(1) because the sorting is performed in-place, using only a fixed number of extra variables regardless of the input size.
