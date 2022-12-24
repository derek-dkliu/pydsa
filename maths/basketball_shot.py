import random

def basic_strategy(p):
    return random.random() < p

def make_strategy(shots, min):
    def strategy(p):
        hits = 0
        for _ in range(shots):
            if random.random() < p:
                hits += 1
        return hits >= min
    return strategy

def run_game(n, p, strategy):
    win = 0
    for _ in range(n):
        if strategy(p): win += 1
    return win

def run_test(n, p):
    strategies = [
        basic_strategy,
        make_strategy(3, 2),
        make_strategy(5, 3)
    ]
    results = {run_game(n, p, s): i + 1 for i, s in enumerate(strategies)}
    scores = list(results.keys())
    winner = results.get(max(scores))
    diffs = [abs(scores[i] - scores[0]) for i in range(1, len(scores))]
    diffstr = ' '.join(map(lambda x: '{:5}'.format(x), diffs))
    print(f"{p:.2f}: {winner}-win, {diffstr}, {scores}")
    
    
for p in [1/4, .5, 2/3]:
    run_test(10000, p)