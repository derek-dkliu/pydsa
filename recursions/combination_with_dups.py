"""Recursion tree"""
def combination(string):
    result = []
    combinate(string, 0, '', result)
    return result

def combinate(string, index, curr, result):
    result.append(curr)
    chosen = set()
    for i in range(index, len(string)):
        c = string[i]
        if c in chosen: continue
        chosen.add(c)
        combinate(string, i + 1, curr + c, result)


if __name__ == '__main__':
    cases = [
        'abc',                  # general
        'a',                    # one
        '',                     # empty
        'aaa'
    ]
    for i, case in enumerate(cases):
        print(f"{'case'.upper()} {i+1}: {case}")
        print(combination(case))