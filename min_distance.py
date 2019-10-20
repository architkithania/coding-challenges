# Problem 23
from copy import deepcopy

class Position: 
    def __init__(self, i, j):
        self.i = i
        self.j = j

def minimum_distance(title_matrix, start, end):
    x, y = start
    start_point = Position(x, y)
    x, y = end
    end_point = Position(x, y)
    min_val = helper(title_matrix, start_point, end_point)
    return min_val

def helper(tile_matrix, pos, end):
    if pos.i == end.i and pos.j == end.j:
        return 0
    
    cant_go = True
    min_len = None

    # Going Left
    if pos.j != 0 and tile_matrix[pos.i][pos.j-1] != True:
        temp_matrix = deepcopy(tile_matrix)
        temp_matrix[pos.i][pos.j] = True
        curr_len = helper(temp_matrix, Position(pos.i, pos.j - 1), end)
        if curr_len is not None:
            curr_len += 1
            if (min_len is None) or min_len > curr_len:
                min_len = curr_len
                cant_go = False
    
    # Going Right
    if pos.j != (len(tile_matrix[0]) - 1) and tile_matrix[pos.i][pos.j+1] != True:
        temp_matrix = deepcopy(tile_matrix)
        temp_matrix[pos.i][pos.j] = True
        curr_len = helper(temp_matrix, Position(pos.i, pos.j + 1), end)
        if curr_len is not None:
            curr_len += 1
            if (min_len is None) or min_len > curr_len:
                min_len = curr_len
                cant_go = False

    # Going Up
    if pos.i != 0 and tile_matrix[pos.i - 1][pos.j] != True:
        temp_matrix = deepcopy(tile_matrix)
        temp_matrix[pos.i][pos.j] = True
        curr_len = helper(temp_matrix, Position(pos.i - 1, pos.j), end)
        if curr_len is not None:
            curr_len += 1
            if (min_len is None) or min_len > curr_len:
                min_len = curr_len
                cant_go = False

    # Going Down
    if pos.i != (len(tile_matrix) - 1) and tile_matrix[pos.i + 1][pos.j] != True:
        temp_matrix = deepcopy(tile_matrix)
        temp_matrix[pos.i][pos.j] = True
        curr_len = helper(temp_matrix, Position(pos.i + 1, pos.j), end)
        if curr_len is not None:
            curr_len += 1
            if (min_len is None) or min_len > curr_len:
                min_len = curr_len
                cant_go = False

    if cant_go:
        return None
    
    return min_len

tile_matrix = [[False, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, False]]
start = [0, 0]
end = [3, 3]
print(minimum_distance(tile_matrix, start, end))