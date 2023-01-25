import threading
import time
from concurrent.futures import ThreadPoolExecutor

"""
Thread:     start(), join()
ThreadPoolExectuor: map(), submit()
Lock:       acquire(), release(), locked()
RLock:      acquire(), release()
Event:      set(), is_set()
Queue:      get(), put(item)
Semaphore:  acquire(), release()
Timer:      start(), cancel()
Barrier:    wait()
"""

def thread_func(name):
	print(f"Thread {name}: starting")
	time.sleep(2)
	print(f"Thread {name}: finishing")

def create_thread():
    print("Main	: before creating thread")
    x = threading.Thread(target=thread_func, args=(1,))
    print("Main	: before running thread")
    x.start()
    print("Main	: wait for the thread to finish")
    x.join()
    print("Main	: all done")

def multiple_threads():
    threads = []
    for i in range(3):
        x = threading.Thread(target=thread_func, args=(i,))
        threads.append(x)
        x.start()
    for i, thread in enumerate(threads):
        print(f"Main    : before joining thread {i}")
        thread.join()
        print(f"Main    : thread {i} done")

def thread_pool_exec():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_func, range(3))

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print(f"Thread {name}: starting update")
        with self._lock:
            value = self.value
            value += 1
            time.sleep(0.1)
            self.value = value
        print(f"Thread {name}: finishing update")

if __name__ == "__main__":
    # create_thread()
    # multiple_threads()
    # thread_pool_exec()

    db = FakeDatabase()
    print(f"Testing update. Starting value is {db.value}.")
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(2):
            executor.submit(db.update, i)
    print(f"Testing update. Ending value is {db.value}.")
