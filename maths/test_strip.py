class Bottle:
    def __init__(self, id, poisoned = False):
        self.id = id
        self.poisoned = poisoned

class TestStrip:
    DAYS_FOR_RESULT = 7

    def __init__(self, id):
        self.id = id
        self.bottles_by_day = []

    def add_drop_on_day(self, bottle, day):
        # create a record of bottles for the target day if not yet exists
        while len(self.bottles_by_day) <= day:
            self.bottles_by_day.append([])
        self.bottles_by_day[day].append(bottle)

    def is_positive_on_day(self, day):
        test_day = day - TestStrip.DAYS_FOR_RESULT + 1
        if test_day < 0 or test_day > len(self.bottles_by_day):
            return False

        for d in range(test_day):
            bottles = self.bottles_by_day[d]
            for bottle in bottles:
                if bottle.poisoned: return True
        return False
        
    def get_last_week_bottles(self, day):
        d =  day - TestStrip.DAYS_FOR_RESULT
        if d < 0:
            raise Exception(f"No bottles tested on day a week before {day}")
        return self.bottles_by_day[d]

def method1(n, m, pid):
    bottles = [Bottle(i) for i in range(n)]
    strips = [TestStrip(i) for i in range(m)]
    bottles[pid].poisoned = True

    day = 0
    while len(bottles) > 1 and len(strips) > 0:
        # add drops on test strips
        i = 0   # strip index
        for bottle in bottles:
            strips[i].add_drop_on_day(bottle, day)
            i = (i + 1) % len(strips)

        # wait for results
        day += TestStrip.DAYS_FOR_RESULT

        # check results
        for strip in strips:
            if strip.is_positive_on_day(day):
                bottles = strip.get_last_week_bottles(day)
                strips.remove(strip)
                break

    if len(bottles) > 1:
        raise Exception("Invalid using method 1")
    poisoned = bottles[0]
    print(poisoned.id == pid, pid, day)

def method2(n, m, pid):
    if n > 1000 or m != 10:
        raise Exception("Only support n <= {1000} and m != {m}")

    bottles = [Bottle(i) for i in range(n)]
    strips = [TestStrip(i) for i in range(m)]
    bottles[pid].poisoned = True

    day = 0
    tests = 3
    while day <= tests:
        for bottle in bottles:
            i = (bottle.id // (10 ** max(2 - day, 0))) % 10
            if day == tests:
                i = (i + 1) % len(strips)
            strips[i].add_drop_on_day(bottle, day)
        day += 1
    
    # get results
    prev = set()   # remember previous results
    digits = [get_positive_on_day(strips, d, prev) for d in range(day)]

    if digits[1] == -1:
        digits[1] = digits[0]
    if digits[2] == -1:
        if digits[3] == -1:
            digits[2] = digits[0] if (digits[0] + 1) % len(strips) == digits[1] else digits[1]
        else:
            digits[2] = (digits[3] - 1 + len(strips)) % len(strips)
    poisoned_id = digits[0] * 100 + digits[1] * 10 + digits[2] 
    days = day - 1 + TestStrip.DAYS_FOR_RESULT
    print(poisoned_id == pid, pid, days)

def get_positive_on_day(strips, test_day, prev):
    result_day = test_day + TestStrip.DAYS_FOR_RESULT
    for strip in strips:
        digit = strip.id
        if strip.is_positive_on_day(result_day) and digit not in prev:
            prev.add(digit)
            return digit
    return -1

def method3(n, m, pid):
    if 2 ** m < n:
        raise Exception('Invalid using binary method')

    bottles = [Bottle(i) for i in range(n)]
    strips = [TestStrip(i) for i in range(m)]
    bottles[pid].poisoned = True

    # add drops to test strips according to binary value of bottle id
    day = 0
    for bottle in bottles:
        for i, d in enumerate(to_bins(bottle.id)):
            if d == 1:
                strips[i].add_drop_on_day(bottle, day)
    
    # wait for resutls
    day += TestStrip.DAYS_FOR_RESULT

    # check results
    poisoned_id = 0
    for i, strip in enumerate(strips):
        if strip.is_positive_on_day(day): 
            poisoned_id |= 1 << i
    print(poisoned_id == pid, pid, day)

def to_bins(num):
    bins = []
    while num != 0:
        bins.append(num & 1)
        num >>= 1
    return bins

import random
n = 1000
m = 10
pid = random.randint(0, n - 1)      # poisoned bottle id
method1(n, m, pid)
method2(n, m, pid)
method3(n, m, pid)
