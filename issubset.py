'''
Given a list, x, determine if a given integer k is a sum of some subset of x.
'''


def is_subset_sum(x: list, k: int) -> bool:
    # If empty list, no k can be formed
    if len(x) == 0:
        return False

    # Create the sum matrix
    sum_matrix = [[False for j in range(0, k + 1)]
                  for i in range(0, len(x) + 1)]

    # Populate the sum matrix
    for i in range(1, len(x)):
        for j in range(0, k + 1):
            result = False or j == x[i - 1]
            result = result or sum_matrix[i - 1][j]
            if j - x[i - 1] > 0:
                result = result or sum_matrix[i - 1][j - x[i - 1]]
            sum_matrix[i][j] = result

    return sum_matrix[len(x)][k]


print(is_subset_sum([1, 2, 3], 3))
