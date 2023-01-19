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
        arr = []
        line = f.readline()
        while line:
            arr.append(int(line))
            line = f.readline()
            if (sys.getsizeof(arr) - 56) > size or not line:
                arr.sort()      # sort arr
                chunk += 1
                cf = open(f"tmp/chunk_{chunk}.txt", "w")            
                cf.writelines(map(lambda x: f"{x}\n", arr))
                cf.close()
                arr = []
    return chunk

def read_file(f, size):
    arr = []
    line = f.readline()
    while line:
        arr.append(int(line))
        if (sys.getsizeof(arr) - 56) > size:
            break
        line = f.readline()
    return arr

def merge_files(chunk, size):
    # open output file
    output = open("tmp/sorted.txt", "w")

    # open files
    files = [open(f"tmp/chunk_{i + 1}.txt") for i in range(chunk)]
    in_size = size // (chunk + 1)
    out_size = in_size * 3

    pq = []
    for f in files:
        arr = read_file(f, in_size)
        heapq.heappush(pq, (arr[0], arr, 0, f))

    sorted = []
    while pq:
        (item, arr, i, f) = heapq.heappop(pq)
        sorted.append(item)
        if (sys.getsizeof(sorted) - 56) > out_size:
            output.writelines(map(lambda x: f"{x}\n", sorted))
            sorted = []
        i += 1
        if i < len(arr):
            heapq.heappush(pq, (arr[i], arr, i, f))
        else:
            arr = read_file(f, in_size)
            if arr:
                heapq.heappush(pq, (arr[0], arr, 0, f))
    if sorted:
        output.writelines(map(lambda x: f"{x}\n", sorted))

    # close output file
    output.close()
    # close files
    for f in files:
        f.close()

file = "tmp/big.txt"
total = 100 * 2 ** 10
round = 10
create_file(file, total, total // round)
chunk_size = os.path.getsize(file) // round

chunk_nums = chunk_file(file, chunk_size)
merge_files(chunk_nums, chunk_size)