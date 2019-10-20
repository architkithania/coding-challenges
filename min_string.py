def minimum_string(str1, str2):
    return helper(str1, str2, "", 0, str2)
    
def helper(str1, str2, res, count, original):
    if res == original:
        return count
    min_val = None
    if len(str1) > 0:

        #Do Nothing
        if str1[0] == str2[0]:
            x = helper(str1[1:], str2[1:], res + str2[0], count, original)
            if min_val is None or x < min_val:
                min_val = x

        #Change
        x = helper(str1[1:], str2[1:], res + str2[0], count + 1, original)
        if min_val is None or x < min_val:
            min_val = x

        #delete
        if len(str1) > 1:
            if str1[1] == str2[0]:
                x = helper(str1[1:], str2[1:], res + str2[0], count + 1, original)
        else:
            x = helper(str1[1:], str2, res, count + 1, original)
        if min_val is None or x < min_val:
            min_val = x

    #Insertion
    x = helper(str1, str2[1:], res + str2[0], count + 1, original)
    if min_val is None or x < min_val
        min_val = x

    return min_val

print(minimum_string("kitten", "sitting"))