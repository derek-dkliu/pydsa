from threading import Lock
from concurrent.futures import ThreadPoolExecutor

def process(curr, max, test1, test2, output, lock):
    while True:
        with lock:
            if curr.get('val') > max:
                return
            if (curr.get('val') % 3 == 0) is test1 and (curr.get('val') % 5 == 0) is test2:
                print(output if (test1 or test2) else curr.get('val'))
                curr['val'] += 1

def fizzbuzz(n):
    lock = Lock()
    curr = {'val': 1}
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(process, curr, n, True, True, 'FizzBuzz', lock)
        executor.submit(process, curr, n, True, False, 'Fizz', lock)
        executor.submit(process, curr, n, False, True, 'Buzz', lock)
        executor.submit(process, curr, n, False, False, '', lock)

fizzbuzz(20)