# with 1GB memory available
def find_missing_int(filepath):
    size = 2 ** 31 // 8
    bitvecs = bytearray(size)
    with open(filepath) as f:
        for line in f:
            num = int(line)
            bitvecs[num // 8] |= 1 << (num % 8)
    for i in range(len(bitvecs)):
        for j in range(8):
            if bitvecs[i] & (1 << j) == 0:
                return i * 8 + j

# with only 10MB memory available
import array

"""
(2-pass file processing)
1. count number of values for each block of range_size from the file
2. find the first block whose number of values less than range_size
3. find the missing value within the block from the file using bit vector

Caculate range_size from 2^31 non-negative integers and 10MB(~2^23) memory
 - since range_size = 2^31 / array_size, and maximum array_size is 2^23 / 4 = 2^21
 - thus 2^10 = 2^31 / 2^21 <= range_size <= 2^23 * 2^3 = 2^26 (max bit vector)
 - ensure minimum use of memory in the process, choose range_size near to the middle, i.e. 2^17

FOLLOW UP - Use even less memory
(3-pass file processing)
1. count for each block of a million elements and choose the first block less than a million
2. count for each sub-block of a thousand elements and choose the first sub-block less than a thousand
3. find the missing value within the sub-block using bit vector
"""
def find_missing_int2(filepath):
    range_size = 1 << 20    # 2^20 bits (2^17 bytes)
    # get count for each block
    blocks = count_block(filepath, range_size)

    # find a block with missing value
    block_index = find_block_index(blocks, range_size)
    if block_index == -1:
        return -1

    # find missing value using bit vector method
    return find_missing_value(filepath, block_index, range_size)
    
def find_missing_value(filepath, block_index, range_size):
    start = block_index * range_size
    end = start + range_size
    bitvecs = bytearray(range_size // 8)
    with open(filepath) as f:
        for line in f:
            num = int(line)
            if num >= start and num < end:
                offset = num - start
                bitvecs[offset // 8] |= 1 << (offset % 8)
    for i in range(len(bitvecs)):
        for j in range(8):
            if bitvecs[i] & (1 < j) == 0:
                return i * 8 + j + start
    return -1

def find_block_index(blocks, range_size):
    for i, count in enumerate(blocks):
        if count < range_size:
            return i
    return -1

def count_block(filepath, range_size):
    nblock = (2 ** 31 - 1) // range_size + 1
    blocks = array.array('i', [0 for i in range(nblock)])
    with open(filepath) as f:
        for line in f:
            num = int(line)
            blocks[num // range_size] += 1
    return blocks
