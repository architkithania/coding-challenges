# Problem 14
import random

def pi_calc():
    prob = prop_calc()
    return 4 * prob

def prop_calc():
    valid_points = 0
    r = 10000000
    for i in range(r):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if in_circle(x, y):
            valid_points += 1
    return valid_points / r

def in_circle(x, y):
    if (x**2 + y**2) < 1.0:
        return True
    return False

print(round(pi_calc(), 3))