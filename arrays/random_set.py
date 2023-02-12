import random

def random_set(arr, m):
    result = set()
    n = len(arr)
    while True:
        i = int(random.random() * n)
        result.add(arr[i])
        if len(result) == m:
            break
    return result

def random_set1(arr, m):
    result = arr[:m]
    for i in range(m, len(arr)):
        k = random.randint(0, i)
        if k < m:
            result[k] = arr[i]
    return result

def random_set2(arr, m):
    for i in range(len(arr)):
        j = random.randint(i, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr[:m]

arr = list(range(20))
print(random_set(arr, 10))
print(random_set1(arr, 10))
print(random_set2(arr, 10))