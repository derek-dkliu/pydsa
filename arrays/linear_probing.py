"""
pros:
1. less wasted space
2. cache friendly
cons:
1. cluster issue
"""
class LinearProbing:
    init_capacity = 10

    def __init__(self, m = 0):
        self.m = m or LinearProbing.init_capacity
        self.n = 0
        self.key = [None] * self.m
        self.val = [None] * self.m

    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        if key is None: raise Exception("None key")
        i = self._hash(key)
        while self.key[i]:
            if self.key[i] == key:
                return self.val[i]
            i = (i + 1) % self.m
        return None

    def put(self, key, val):
        if key is None: raise Exception("None key")
        if val is None:
            self.delete(key)
            return

        # double table size if 50% full
        if self.n >= self.m / 2:
            self._resize(self.m * 2) 

        i = self._hash(key)
        while self.key[i]:
            if self.key[i] == key:
                self.val[i] = val
                return
            i = (i + 1) % self.m
        self.key[i] = key
        self.val[i] = val
        self.n += 1

    def delete(self, key):
        if key is None: raise Exception("None key")
        if not self.contains(key): return

        i = self._hash(key)
        # find key position i
        while self.key[i] != key:
            i = (i + 1) % self.m
        # delete key and associated value
        self.key[i] = None
        self.val[i] = None
        self.n -= 1
        # rehash keys in same cluster after deleted key
        i = (i + 1) % self.m
        while self.key[i]:
            k = self.key[i]
            v = self.val[i]
            self.key[i] = None
            self.val[i] = None
            self.n -= 1
            self.put(k, v)
            i = (i + 1) % self.m
        
        # halve table size if less than 12.5% full
        if self.m > LinearProbing.init_capacity and self.n <= self.m / 8:
            self._resize(self.m // 2)
        
    def _resize(self, capacity):
        temp = LinearProbing(capacity)
        for i in range(self.m):
            if self.key[i]:
                temp.put(self.key[i], self.val[i])
        self.key = temp.key
        self.val = temp.val
        self.m = temp.m
        self.n = temp.n

    def _hash(self, key):
        return hash(key) % self.m

    def __len__(self):
        return self.n

    def __str__(self):
        out = ''
        for i in range(self.m):
            item = f"{self.key[i]}|{self.val[i]}" if self.key[i] else None
            out += f"{i}: {item}\n"
        return out

if __name__ == '__main__':
    hashmap = LinearProbing()
    for i in range(65, 80):
        hashmap.put(chr(i), i)
    print(hashmap)
    print(len(hashmap))
