class CircularArray:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.head = 0

    def rotate(self, shift):
        self.head = self.convert(shift)

    def __getitem__(self, index):
        return self.arr[self.convert(index)]

    def __setitem__(self, index, value):
        self.arr[self.convert(index)] = value

    def __delitem__(self, index):
        # del self.arr[self.convert(index)]
        self.arr[self.convert(index)] = None

    def __len__(self):
        return len(self.arr)

    def __iter__(self):
        self._offset = 0
        return self
    
    def __next__(self):
        if self._offset == len(self.arr):
            raise StopIteration
        else:
            item = self.arr[self.convert(self._offset)]
            self._offset += 1
            return item

    def convert(self, index):
        return (self.head + index) % len(self.arr)


ca = CircularArray(6)
ca[0] = 1
ca[1] = 2
ca[2] = 3
ca[3] = 4
ca[4] = 5
del ca[3]
ca.rotate(2)
for a in ca: print(a)

