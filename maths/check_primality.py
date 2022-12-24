import math

"""
check if a number is prime number.
check if it is divisible by any one of numbers 
from 2 to n-1 (better sqrt(n)), if so, it is not, otherwise true.
"""
# time:  O(sqrt(n))
# space: O(1)
def check_primality(n):
    if n < 2: return False
    sqrt = math.floor(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

for n in [0,1,2,25,26,29,99]:
    print(n, check_primality(n))