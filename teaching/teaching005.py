import random

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Generate a list of 10 random numbers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]

print("Original array is", arr)
print("Sorted array is", selection_sort(arr))

