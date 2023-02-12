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
Idea: distribute numbers into fixed size buckets of a certain range, 
any non-full bucket contains the missing integer, use bit vector to find it

(2-pass file processing)
1. count number of values for each bucket of range_size from the file
2. find the first bucket whose number of values less than range_size
3. find the missing value within the bucket from the file using bit vector

Caculate range_size from 2^31 non-negative integers and 10MB(~2^23) memory
 - since range_size = 2^31 / array_size, and maximum array_size is 2^23 / 4 = 2^21
 - thus 2^10 = 2^31 / 2^21 <= range_size <= 2^23 * 2^3 = 2^26 (max bit vector)
 - to ensure minimum use of memory, choose range_size which balance the following:
   - memory used for buckets     = 2^31 / range_size * 2^2
   - memory used for bit vectors = range_size / 2^3
 - so x^2 = 2^36, thus x = 2^18


FOLLOW UP - Use even less memory
(3-pass file processing)
1. count for each bucket of a million elements and choose the first bucket less than a million
2. count for each sub-bucket of a thousand elements and choose the first sub-bucket less than a thousand
3. find the missing value within the sub-bucket using bit vector
"""
def find_missing_int2(filepath):
    range_size = 1 << 18
    # get count for each bucket
    buckets = count_bucket(filepath, range_size)

    # find a bucket with missing value
    bucket_index = find_bucket_index(buckets, range_size)
    if bucket_index == -1:
        return -1

    # find missing value using bit vector method
    return find_missing_value(filepath, bucket_index, range_size)
    
def find_missing_value(filepath, bucket_index, range_size):
    start = bucket_index * range_size
    end = start + range_size
    bitvecs = bytearray(range_size // 8 + 1)
    with open(filepath) as f:
        for line in f:
            num = int(line)
            if num >= start and num < end:
                offset = num - start
                bitvecs[offset // 8] |= 1 << (offset % 8)
    for i in range(len(bitvecs)):
        for j in range(8):
            if bitvecs[i] & (1 << j) == 0:
                return i * 8 + j + start
    return -1

def find_bucket_index(buckets, range_size):
    for i, count in enumerate(buckets):
        if count < range_size:
            return i
    return -1

def count_bucket(filepath, range_size):
    nbucket = (2 ** 31 - 1) // range_size + 1
    buckets = array.array('i', [0 for i in range(nbucket)])
    with open(filepath) as f:
        for line in f:
            num = int(line)
            buckets[num // range_size] += 1
    return buckets
