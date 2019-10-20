nums = []

def function(nums, x):
    if len(nums) % 2 == 1:
        return nums[(len(nums) - 1)//2]
    else:
        mid = (len(nums) - 1)//2
        return (nums[mid] + nums[mid + 1])/2

for x in range(1000):
    nums.append(x)
    nums.sort()
    print(function(nums, x))

    