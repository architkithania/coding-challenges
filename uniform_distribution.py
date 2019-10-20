# Problem 15
import random

def random_num(big_stream):
    random_num = None
    for i in range(0, len(big_stream)):
        if i == 0:
            random_num = big_stream[i]
        else:
            if random.randint(0,1) == 0:
                random_num = big_stream[i]
    return random_num

def counter(big_stream):
    counters = []
    for e in big_stream:
        counters.append(0)
    for i in range(1000000):
        num = random_num(big_stream)
        counters[num] += 1
    print(counters)

counter([0, 1, 2, 3, 4]) 