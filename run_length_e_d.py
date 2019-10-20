def encoding(string):
    encoded = ""
    count = 0
    prev_char = ""
    for char in string:
        if prev_char == char:
            count += 1
        else:
            if prev_char != "":
               encoded += str(count) + prev_char
            prev_char = char
            count = 1
    encoded += str(count) + prev_char
    return encoded

def decoding(encoded):
    decoded = ""
    encode_list = list(encoded)
    i = 0
    while i < len(encode_list) - 1:
        repeat = 0
        if encode_list[i].isdigit() and encode_list[i+1].isdigit():
            repeat = int(encode_list[i] + encode_list[i+1])
            i += 1
        else:
            repeat = int(encode_list[i])
        for j in range(repeat):
            decoded += encode_list[i+1]
        i += 2
    return decoded