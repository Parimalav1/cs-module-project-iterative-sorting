import time

start_time = time.time()


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
        # for item in arr:
        # if item == target:
            return i

    return -1   # not found


arr = [4, 3, 10, 56, 38, 39, 2, 15, 8, 54]
arr = range(1000000)
linear_search(arr, 999999)
end_time = time.time()
print(f'runtime: {end_time - start_time}seconds')

start_time = time.time()
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        estimate = arr[middle]
        if estimate == target:
            return middle
        if estimate > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1  # not found


test_list = [2, 4, 7, 8, 9, 10, 12, 34, 45]
test_list = range(1000000)

binary_search(test_list, 999999)
# 2
# >>> binary_search(test_list, 34)
# 7

end_time = time.time()
print(f'runtime: {end_time - start_time}seconds')
