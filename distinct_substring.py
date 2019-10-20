# Problem 13
def sub_string(string, k):
    maximum = 0
    for i in range(0,len(string) - 1):
        dist = []
        x = helper(string[i:], k, 0, dist)
        if maximum < x:
            maximum = x
    return maximum

def helper(string, k, length, dist):
    if k == 0:
        return length
    if len(string) > 1:
        sub_str = string[1:]
        if string[0] not in dist:
            dist.append(string[0])
        if string[1] in dist:
            return helper(sub_str, k, length + 1, dist)
        return helper(sub_str, k - 1, length + 1, dist)
    else:
        return length