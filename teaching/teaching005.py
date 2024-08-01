import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ask the user for the number of elements in the array
n = int(input("请输入数组的元素个数: "))

# Generate an array of n random integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(n)]

print("Original array is", arr)
print("Sorted array is", selection_sort(arr))

