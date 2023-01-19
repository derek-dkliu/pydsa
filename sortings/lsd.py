'''
sort keys of integer or string by its each digit starting from 
the least significant place, using buckets and counts.
'''
# time:  O(kn)  where n is the number of keys, k is the fixed length of the key
# space: O(R)   where R is aplhabet size of the keys
def lsd(arr):
    R = 256
    k = len(arr[0])
    aux = [None] * len(arr)
    for d in range(k - 1, -1, -1):
        count = [0] * (R + 1)
        # count frequency
        for item in arr:
            count[ord(item[d]) + 1] += 1
        # cumulate count
        for i in range(R):
            count[i + 1] += count[i]
        # move data
        for item in arr:
            c = ord(item[d])
            aux[count[c]] = item
            count[c] += 1
        # copy back
        for i in range(len(arr)):
            arr[i] = aux[i]

# sort 32-bit integers
def lsd_int(arr):
    BITS = 8
    k = 4
    R = 1 << BITS
    mask = R - 1
    aux = [None] * len(arr)
    for p in range(k):
        count = [0] * (R + 1)
        shift = p * BITS
        for item in arr:
            c = (item >> shift) & mask
            count[c + 1] += 1
        for i in range(R):
            count[i + 1] += count[i]

        # for most significant bytes, [0x80 - 0xff] comes before [0x00 - 0x7f]
        if p == k - 1:
            upper = count[R] - count[R // 2]
            lower = count[R // 2]
            for i in range(R // 2):
                count[i] += upper
            for i in range(R // 2, R):
                count[i] -= lower

        for item in arr:
            c = (item >> shift) & mask
            aux[count[c]] = item
            count[c] += 1
        for i in range(len(arr)):
            arr[i] = aux[i]


arr = ['test', 'anne', 'pete', 'erin', 'eric', 'jimy']
print(arr)
lsd(arr)
print(arr)

import random
arr = list(range(15))
arr.extend([-1, -3, -5])
random.shuffle(arr)
print(arr)
lsd_int(arr)
print(arr)
