def find_one(arr):
    bit_max = len(bin(max(arr))) - 2
    bit_set = [0 for i in range(bit_max)]
    for num in arr:
        index = len(bit_set) - 1
        temp_num = num
        while temp_num != 0:
            bit_set[index] += temp_num & 1
            temp_num = temp_num >> 1
            index -= 1
    bit_set = [str(val % 3) for val in bit_set]
    bit_set = "".join(bit_set)
    return int(bit_set, 2)

print(find_one([16, 15, 15, 16, 16, 14, 15]))