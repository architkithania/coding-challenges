class Dimensions:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Mate:
    def __init__(self, dim, is_alive=True):
        self.dim = dim
        self.is_alive = is_alive
    
    def kill(self):
        self.is_alive = False

def conways_life(start_coords, steps):
    alive_mates = []
    for coord in start_coords:
        alive_mates.append(Dimensions(coord[0], coord[1]))
    for i in range(steps):
        i = 0
        arr_len = len(alive_mates)
        while i < arr_len:
            neighbours = get_neighbours(alive_mates[i], alive_mates)
            if neighbours < 2 or neighbours > 3:
                alive_mates.pop(i)
                arr_len -= 1
            new_cell_loc = one_of_three(alive_mates[i], alive_mates)
            if new_cell_loc.x is not None:
                alive_mates.append(new_cell_loc)
        print_board(alive_mates)

def get_neighbours(mate, alive_mates):
    neighbours = 0
    for i in alive_mates:
        if i.x == mate.x and (i.y == mate.y + 1 or i.y == mate.y - 1):
            neighbours += 1
        elif i.y == mate.y and (i.x == mate.x + 1 or i.x == mate.x - 1):
            neighbours += 1
        elif i.x == mate.x + 1 and (i.y == mate.y + 1 or i.y == mate.y - 1):
            neighbours += 1
        elif i.x == mate.x - 1 and (i.y == mate.y + 1 or i.y == mate.y - 1):
            neighbours += 1
    return neighbours

def one_of_three(mate, alive_mates):
    