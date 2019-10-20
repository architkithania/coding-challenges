def binary_search(arr, start, end, val):
    if end < start:
        return None
    mid = start + (end - start) // 2
    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        return binary_search(arr, mid + 1, end, val)
    return binary_search(arr, start, mid - 1, val)

