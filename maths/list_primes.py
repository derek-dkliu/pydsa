# time:  O(n*log(log n))
# space: O(n)
def list_primes1(n):
    if n < 1: return None

    # set all numbers to be prime other than 0 and 1
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    
    for i in range(2, n + 1):
        # next prime number i
        if prime[i]:
            # cross out all multiples of prime number i
            for j in range(2, n // i + 1):
                prime[i * j] = False
    return prime

import math
def list_primes2(n):
    if n < 1: return None
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    
    sqrt = math.floor(math.sqrt(n))
    # can end earlier at sqrt(n) since j start from i (see below) and i * j <= n, thus i * i <= n
    for i in range(2, sqrt + 1):
        if prime[i]:
            # start j from i since any i * j (when j < i) have been checked before
            # end j at n // i since i * j must be within the index of the prime list
            for j in range(i, n // i + 1):
                prime[i * j] = False
    return prime

def list_primes3(n):
    if n < 1: return None
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    
    sqrt = math.floor(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if prime[i]:
            # same as above but easier to read
            j = i * i
            while j <= n:
                prime[j] = False
                j += i      # next multiple of i
    return prime

def equal(t1, t2):
    return all([v1 == v2 for v1, v2 in zip(t1, t2)])

n = 200
print(equal(list_primes1(n), list_primes2(n)))
print(equal(list_primes1(n), list_primes3(n)))