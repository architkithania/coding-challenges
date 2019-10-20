def get_subsets(arr, k):
    for i in range(0, len(arr) - k + 1):
        print(arr[i:i+k])
        print(max(arr[i:i+k]))

get_subsets([10, 5, 2, 7, 8, 7], 3)

            
        