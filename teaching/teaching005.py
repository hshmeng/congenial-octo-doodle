import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [random.randint(1, 100) for _ in range(10)]

print("Original array is", arr)
print("Sorted array is", selection_sort(arr))

