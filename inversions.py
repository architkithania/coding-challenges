'''
Given an array of distinct elements, return the number of inversions in 
less than O(n^2) time

An inversion pair (A[i], A[j]) is pair such that A[i] > A[j] and i < j
'''


def merge_sort(arr, count):
    if len(arr) <= 2:
        if len(arr) == 2 and arr[0] > arr[1]:
            count += 1
            return sorted(arr), count
        return sorted(arr), count
    middle = len(arr) // 2
    left, left_count = merge_sort(arr[:middle], count)
    right, right_count = merge_sort(arr[middle:], count)
    left_ptr = 0
    right_ptr = 0
    result = []
    while left_ptr != len(left) or right_ptr != len(right):
        if left_ptr != len(left) and right_ptr != len(right):
            if left[left_ptr] <= right[right_ptr]:
                result.append(left[left_ptr])
                left_ptr += 1
            else:
                result.append(right[right_ptr])
                right_count += 1
                right_ptr += 1
        elif left_ptr != len(left):
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1
    return result, left_count + right_count


print(merge_sort([2, 4, 1, 3, 5], 0))
