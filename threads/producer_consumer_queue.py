import random
import logging
import time
from queue import Queue
from threading import Event
from concurrent.futures import ThreadPoolExecutor

class Pipeline(Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug(f"{name}: about to get from queue")
        value = self.get()
        logging.debug(f"{name}: got {value} from queue")
        return value

    def set_message(self, value, name):
        logging.debug(f"{name}: about to add {value} to queue")
        self.put(value)
        logging.debug(f"{name}: added {value} to queue")

def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 100)
        logging.info(f"Producer got message: {message}")
        pipeline.set_message(message, 'Producer')
    logging.info(f"Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message('Consumer')
        logging.info(f"Consumer storing message: {message} (queue size={pipeline.qsize()}")
    logging.info(f"Consumer received EXIT event. Exiting")


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s: %(message)s", datefmt="%H:%M:%S",
                        level=logging.INFO)
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.01)
        logging.info("Main: about to set event")
        event.set()
