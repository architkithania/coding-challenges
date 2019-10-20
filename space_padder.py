def word_line(words, k):
    count = 0
    index = 0
    word_lines = []
    for word in words:
        if count + len(word) + 1 <= k: 
            if len(word_lines) < index + 1:
                word_lines.append([])
                word_lines[index].append(word)
                count += len(word) + 1
            else:
                word_lines[index].append(word)
                count += len(word) + 1
        else:
            index += 1 
            word_lines.append([])
            word_lines[index].append(word)
            count = len(word) + 1
    return word_lines

def padder(words, k):
    lines = word_line(words, k)
    padded = []
    for line in lines:
        line_str = ""
        line_len = 0
        for i, e in enumerate(line[:-1]):
            line[i] = e + " "
            line_len += len(line[i])
        line_len += len(line[-1])
        index = 0
        while line_len < k:
            line[index] += " "
            line_len += 1
            index += 1
            if index >= len(line) - 1:
                index = 0
        line_str = "".join(line)
        line_str = line_str.strip()
        while len(line_str) != k:
            line_str += ' '
        padded.append(line_str)
    return padded

print(padder(["dog"], 16))