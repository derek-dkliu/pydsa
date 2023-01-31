# time:  O(n logn), where n is the number of people
# space: O(n)
def living_people(people, min, max):
    births = []
    deaths = []
    for b, d in people:
        births.append(b)
        deaths.append(d)
    births.sort()
    deaths.sort()

    max_alive = 0
    max_year = 0
    alive = 0
    i = 0
    j = 0
    while i < len(births) and j < len(deaths):
        if births[i] <= deaths[j]:
            alive += 1
            if alive > max_alive:
                max_alive = alive
                max_year = births[i]
            i += 1
        else:
            alive -= 1
            j += 1
    return max_year, max_alive
        

# time:  O(n + m), where n is the number of people, m is the range of the years
# space: O(m)
def living_people2(people, min, max):
    changes = [0] * (max - min + 2)
    for b, d in people:
        changes[b - min] += 1
        changes[d - min + 1] -= 1
    max_alive = 0
    max_year = 0
    alive = 0
    for i, change in enumerate(changes):
        alive += change
        if alive > max_alive:
            max_alive = alive
            max_year = i + min
    return max_year, max_alive


people = [
    [1912, 1915],
    [1920, 1990],
    [1910, 1998], 
    [1901, 1972],
    [1910, 1998],
    [1923, 1982],
    [1913, 1998],
    [1990, 1998],
    [1983, 1999],
    [1975, 1994],
]
print(living_people(people, 1900, 2000))
print(living_people2(people, 1900, 2000))