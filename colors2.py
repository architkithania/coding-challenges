# Problem 19
def min_cost(cost_matrix, num, k):
    min_val = None
    for i in range(0, k):
        x = helper(cost_matrix, num - 1, i, False)
        if min_val == None or min_val > x:
            min_val = x
    for i in range(0, k):
        x = helper(cost_matrix, 0, i, True)
        if x < min_val:
            min_val = x
    return x

def helper(cost_matrix, n, k, reverse):
    if reverse:
        if n == (len(cost_matrix) - 1):
            min_val = None
            for i, e in enumerate(cost_matrix[n]):
                if i != k:
                    if min_val == None or e < min_val:
                        min_val = e
            return min_val
        min_val = None
        for i, e in enumerate(cost_matrix[n]):
            if i != k:
                x = helper(cost_matrix, n + 1, i, True)
                if min_val == None or min_val > x:
                    min_val = x
        return x
    else:
        if n == 0:
            min_val = None
            for i, e in enumerate(cost_matrix[n]):
                if i != k:
                    if min_val == None or e < min_val:
                        min_val = e
            return min_val
        min_val = None
        for i, e in enumerate(cost_matrix[n]):
            if i != k:
                x = helper(cost_matrix, n - 1, i, False)
                if min_val == None or min_val > x:
                    min_val = x
        return x
            


