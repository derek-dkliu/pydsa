import random

def simulate(nfamily):
    ngirl = 0
    nboy = 0
    for _ in range(nfamily):
        g, b = one_family()
        ngirl += g
        nboy += b
    return ngirl / nboy, ngirl, nboy

def one_family():
    girl = 0
    boy = 0
    while girl == 0:
        if random.random() < 0.5:
            girl += 1
        else:
            boy += 1
    return (girl, boy)

r, g, b = simulate(1000000)
print(f"G:B={r}, G={g}, B={b}")