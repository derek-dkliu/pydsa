# time:  O(n*2^n)
# space: O(n*2^n)
def power_set(arr):
    result = []
    ps(arr, 0, [], result)
    return result

def ps(arr, index, curr, result):
    if index == len(arr):
        result.append(curr[:])
        return
    ps(arr, index+1, curr, result)
    curr.append(arr[index])
    ps(arr, index+1, curr, result)
    curr.pop()

def power_set2(arr):
    return ps2(arr, 0)

def ps2(arr, index):
    if index == len(arr): return[[]]

    result = []
    for subset in ps2(arr, index + 1):
        result.append(subset)
        result.append([arr[index]] + subset)
    return result

A = list(range(6))
print(len(power_set(A)))
print(len(power_set2(A)))
