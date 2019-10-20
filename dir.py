def plus_one(digits):
    num = 0
    for i, e in enumerate(digits):
        num += e * (10 ** (len(digits) - (i + 1)))
    return num + 1

print(plus_one([9, 9, 9, 9]))