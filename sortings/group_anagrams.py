def group_anagrams(arr):
    arr.sort(key = lambda x:sorted(x))

def group_anagrams2(arr):
    map = {}
    for s in arr:
        key = bucket_key(s)
        print(s, key)
        if key not in map:
            map[key] = [s]
        else:
            map[key].append(s)
    index = 0
    for values in map.values():
        for s in values:
            arr[index] = s
            index += 1

def sort_key(s):
    return ''.join(sorted(s))

def bucket_key(s):
    buckets = [0] * 26
    for c in s:
        buckets[ord(c) - ord('a')] += 1
    sb = []
    for i, c in enumerate(buckets):
        if c > 0:
            sb.append(chr(i + ord('a')) + str(c))
    return ''.join(sb)

arr = ['abc', 'dca', 'bca', 'cab', 'acc', 'adc']
group_anagrams(arr)
print(arr)

arr = ['abc', 'dca', 'bca', 'cab', 'acc', 'adc']
group_anagrams2(arr)
print(arr)