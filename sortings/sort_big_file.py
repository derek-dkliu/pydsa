import math
import random
import os, sys, heapq

def create_file(file, total, block):
    chunk = math.ceil(total / block)
    with open(file, "w") as f:
        for i in range(chunk):
            size = total % (block + 1) if i == chunk - 1 else block
            for num in random.sample(range(1, total + 1), size):
                f.write(str(num) + '\n')

"""
External merge sort:
Divide the big file into k chunks, the size of each chunk equals x, the amount of memory available.
Each chunk is sorted and saved back to a temp file.
Read y = x / (k + 1) of each sorted chunk into input buffers in main memory, and allocate remaining y
for the output buffer. Perform a k-way merge and store the result in the output buffer. Whenever the
output buffer is full, write it to the final sorted file and empty it. Whenever any one of the input buffer
is empty, fill it with next y part of its associated sorted chunk unitl no more data from the chunk is available.
"""

def chunk_file(file, size):
    chunk = 0 
    with open(file) as f:
        while True:
            arr = read_by_size(f, size)
            if not arr:
                break
            arr.sort()
            chunk += 1
            with open(f"tmp/chunk_{chunk}.txt", "w") as cf:
                cf.writelines(map(lambda x: f"{x}\n", arr))
    return chunk

def merge_files(chunk, size):
    # open output file
    output = open("tmp/sorted.txt", "w")

    # open files
    files = [open(f"tmp/chunk_{i + 1}.txt") for i in range(chunk)]
    buffer_size = size // (chunk + 1)   # sorted buffer count as one more chunk

    pq = []
    for f in files:
        arr = read_by_size(f, buffer_size)
        heapq.heappush(pq, (arr[0], arr, 0, f))

    full = len(pq)
    sorted = []         # sorted buffer
    while pq:
        (item, arr, i, f) = heapq.heappop(pq)
        sorted.append(item)
        if len(sorted) == full:
            output.writelines(map(lambda x: f"{x}\n", sorted))
            sorted = []
        if i == len(arr) - 1:
            arr = read_by_size(f, buffer_size)
            if arr:
                heapq.heappush(pq, (arr[0], arr, 0, f))
        else:
            i += 1
            heapq.heappush(pq, (arr[i], arr, i, f))
        
    if sorted:
        output.writelines(map(lambda x: f"{x}\n", sorted))

    # close output file
    output.close()
    # close files
    for f in files:
        f.close()

def read_by_size(f, size):
    arr = []
    for line in f.read(size).split('\n'):
        if line:
            arr.append(int(line))
    return arr

file = "tmp/big.txt"
total = 100 * 2 ** 10
round = 10
create_file(file, total, total // round)
chunk_size = os.path.getsize(file) // round

chunk_nums = chunk_file(file, chunk_size)
merge_files(chunk_nums, chunk_size)