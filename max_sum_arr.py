from typing import List
from math import inf


def max_sum_arr(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    running_sum = -inf
    max_so_far = 0.0
    for num in arr:
        if num >= running_sum + num:
            running_sum = num
        else:
            max_so_far = max(running_sum, running_sum + num)
            running_sum += num
    return max(0, int(max_so_far))
