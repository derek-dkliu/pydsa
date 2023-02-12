"""can only access each bit of each integer"""

# time:  O(n)
def missing_integer(arr):
    return missing_int(arr, 0)

def missing_int(arr, d):
    if len(arr) == 0:
        return 0

    ones = []
    zeros = []
    for num in arr:
        if num & 1 << d != 0:
            ones.append(num)
        else:
            zeros.append(num)
    
    if len(zeros) <= len(ones):
        v = missing_int(zeros, d + 1)
        return v << 1
    else:
        v = missing_int(ones, d + 1)
        return v << 1 | 1

import random
def generate_arr(n):
    arr = list(range(n))
    random.shuffle(arr)
    return arr[1:], arr[0]

for n in [10, 20, 50, 100, 100]:
    arr, t = generate_arr(n)
    # print(arr, t)
    print(missing_integer(arr) == t)