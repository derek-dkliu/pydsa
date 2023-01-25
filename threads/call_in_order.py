from threading import Lock, Semaphore, current_thread
from concurrent.futures import ThreadPoolExecutor
import time

class CallInOrder:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self):
        self.lock1.acquire()
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.lock2.release()

    def second(self):
        self.lock2.acquire()
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.lock3.release()

    def third(self):
        self.lock3.acquire()
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.lock1.release()


class CallInOrder2:
    def __init__(self):
        self.sem1 = Semaphore(1)
        self.sem2 = Semaphore(1)
        self.sem1.acquire()
        self.sem2.acquire()

    def first(self):
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.sem1.release()

    def second(self):
        self.sem1.acquire()
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.sem1.release()
        self.sem2.release()

    def third(self):
        self.sem2.acquire()
        print(f"{current_thread().getName()}: running")
        time.sleep(.1)
        self.sem2.release()

cio = CallInOrder2()
with ThreadPoolExecutor(max_workers=3) as executor:
    for _ in range(2):
        executor.submit(cio.first)
        executor.submit(cio.second)
        executor.submit(cio.third)

