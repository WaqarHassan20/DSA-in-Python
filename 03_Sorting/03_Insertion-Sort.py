array = [8, 7, 2, 5, 4, 6, 3, 9, 1]
length = len(array)

print("Unsorted Array", array)

def insertion_sort_ascending(arr):
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort_ascending(array)
print("Ascending Order", array)


def insertion_sort_descending(arr):
    for i in range(1,length):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] < key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort_descending(array)
print("Descending Order", array)
