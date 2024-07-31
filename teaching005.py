def bubble_sort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n-1):
        # 最后 i 个元素已经到位
        for j in range(0, n-i-1):

            # 遍历数组从 0 到 n-i-1
            # 如果发现当前元素比下一个元素大
            # 则交换两个元素
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 测试函数
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print ("排序后的数组是：")