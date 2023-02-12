from array import array

def find_duplicates(arr):
    bv = BitVector(3200)
    for num in arr:
        if bv.has(num):
            print(num)
        else:
            bv.add(num)
        
class BitVector:
    def __init__(self, size):
        self.bv = array('i', [0] * ((size >> 5) + 1))

    def add(self, num):
        self.bv[num >> 5] |= 1 << (num & 0x1f)

    def has(self, num):
        return self.bv[num >> 5] & (1 << (num & 0x1f)) != 0

import random
arr = random.choices(range(20), k=25)
print(arr)
find_duplicates(arr)