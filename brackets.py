def matcher(string):
    must_close = []
    for char in string:
        if is_opener(char):
            must_close.insert(0, char_invert(char))
        else:
            if must_close[0] != char:
                return False
            else:
                del(must_close[0])
    if len(must_close) == 0:
        return True
    else:
        return False

def is_opener(char):
    if char == '[' or char == '{' or char == '(':
        return True
    return False

def char_invert(char):
    if char == '(':
        return ")"
    if char == "[":
        return "]"
    if char == "{":
        return "}"