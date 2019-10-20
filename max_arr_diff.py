from math import isinf
from typing import List


def max_arr_diff(arr: List[int]) -> int:
    if len(arr) < 2:
        return 0
    min_element = arr[0]  # type: int
    max_diff = float("-inf")
    for num in arr[1:]:
        if num - min_element > max_diff:
            max_diff = num - min_element
        if num < min_element:
            min_element = num
    if isinf(max_diff):
        return 0
    return int(max_diff)


print(max_arr_diff([9, 11, 8, 5, 7, 10]))
