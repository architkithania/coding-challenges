# Problem 12
def init(n):
    arr = []
    for i in range(0,n):
        arr.append(0)
    return num_of_ways(n, arr)

def num_of_ways(n, arr):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if arr[n-1] != 0:
        return arr[n-1]
    arr[n-1] = num_of_ways(n-1, arr)
    arr[n-2] = num_of_ways(n-2, arr)
    return arr[n-1] + arr[n-2]

def init_2(n):
    arr = []
    for i in range(0,n):
        arr.append(0)
    X = [5, 3, 2]
    X.sort()
    return num_of_ways_2(n, arr, X)

def num_of_ways_2(n, arr, X):
    if n == 0:
        return 1
    if n < X[0]:
        return len(X)
    if arr[n-1] != 0:
        return arr[n-1]
    sum = 0
    for i in X:
        if i <= n:
            sum += num_of_ways_2(n - i, arr, X)
        sum += len(X) - (X.index(i) + 1)
    arr[n-1] = sum
    return sum