import math

def get_interval_quadratic_formula(a, b, c):
    d = b ** 2 - 4 * a * c
    sol1 = (-b + d ** 0.5) / (2 * a)
    sol2 = (-b - d ** 0.5) / (2 * a)
    return math.ceil(max(sol1, sol2))

def find_breakpoint(floors, breakpoint):
    # calculate interval by solving x(x+1)/2 = floors
    interval = get_interval_quadratic_formula(1, 1, -2 * floors)
    egg1 = interval
    prevfloor = 0
    count = 0

    # drop egg1 at decreasing intervals
    while True:
        count += 1
        if egg1 >= breakpoint:
            break
        interval -= 1
        prevfloor = egg1
        egg1 = min(egg1 + interval, floors)
    
    # drop egg2 at one unit increments
    egg2 = prevfloor + 1
    while egg2 < egg1:
        count += 1
        if egg2 >= breakpoint:
            break
        egg2 += 1

    if egg2 > floors:
        raise Exception("No breaking floor!")
    print(breakpoint == egg2, egg2, count)

import random
floors = 100
r = random.randint(1, floors)
for breakpoint in [1, 14, 99, 100, r]:
    find_breakpoint(floors, breakpoint)