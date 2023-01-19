def group_anagrams(arr):
    arr.sort(key = lambda x:sorted(x))

def group_anagrams2(arr):
    map = {}
    for s in arr:
        key = sort(s)
        if key not in map:
            map[key] = [s]
        else:
            map[key].append(s)
    index = 0
    for values in map.values():
        for s in values:
            arr[index] = s
            index += 1

def sort(s):
    return ''.join(sorted(s))

arr = ['abc', 'dca', 'bca', 'cab', 'acc', 'adc']
group_anagrams(arr)
print(arr)

arr = ['abc', 'dca', 'bca', 'cab', 'acc', 'adc']
group_anagrams2(arr)
print(arr)