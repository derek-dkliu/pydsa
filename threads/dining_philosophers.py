from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import time
import logging

class Philosopher:
    def __init__(self, id, chopsticks):
        self.id = id
        self.starve_count = 0
        self.left = chopsticks[id]
        self.right = chopsticks[(id + 1) % len(chopsticks)]

    def eat(self):
        while True:
            if not self.pickup_left():
                self.starve_count += 1
                logging.info(f'Phil {self.id}: starving {self.starve_count}')
                time.sleep(1)
                continue
            self.pickup_right()
            self.chew()
            self.putdown_right()
            self.putdown_left()
            break

    def chew(self):
        logging.info(f'Phil {self.id}: started eating')
        time.sleep(2)
        logging.info(f'Phil {self.id}: finished eating')

    def pickup_left(self):
        self.left.acquire()
        logging.info(f'Phil {self.id}: picked up left chopstick')
        if self.right.locked():
            self.putdown_left()
            return False
        return True

    def pickup_right(self):
        self.right.acquire()
        logging.debug(f'Phil {self.id}: picked up right chopstick')

    def putdown_left(self):
        self.left.release()
        logging.info(f'Phil {self.id}: put down left chopstick')

    def putdown_right(self):
        self.right.release()
        logging.info(f'Phil {self.id}: put down right chopstick')

# breaking potential deadlock by reversing pickup order of chopsticks for the last one
class Philosopher2:
    def __init__(self, id, chopsticks):
        self.id = id
        if id == len(chopsticks) - 1:
            self.left = chopsticks[0]
            self.right = chopsticks[id]
        else:
            self.left = chopsticks[id]
            self.right = chopsticks[id + 1]

    def eat(self):
        self.pickup_left()
        self.pickup_right()
        self.chew()
        self.putdown_right()
        self.putdown_left()

    def chew(self):
        logging.info(f'Phil {self.id}: started eating')
        time.sleep(2)
        logging.info(f'Phil {self.id}: finished eating')

    def pickup_left(self):
        self.left.acquire()
        logging.info(f'Phil {self.id}: picked up left chopstick')

    def pickup_right(self):
        self.right.acquire()
        logging.debug(f'Phil {self.id}: picked up right chopstick')

    def putdown_left(self):
        self.left.release()
        logging.info(f'Phil {self.id}: put down left chopstick')

    def putdown_right(self):
        self.right.release()
        logging.info(f'Phil {self.id}: put down right chopstick')


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s: %(message)s", datefmt="%H:%M:%S",
                        level=logging.INFO)
    logging.getLogger().setLevel(logging.DEBUG)

    total = 5
    chopsticks = [Lock() for _ in range(total)]
    # philosophers = [Philosopher(i, chopsticks) for i in range(total)]
    philosophers = [Philosopher2(i, chopsticks) for i in range(total)]
    with ThreadPoolExecutor(max_workers=total) as executor:
        for philosopher in philosophers:
            executor.submit(philosopher.eat)