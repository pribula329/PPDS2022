from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore


class Shared():
    def __init__(self, size):
        self.finished = False
        self.mutex = Mutex()
        self.items = Semaphore(0)
        self.free = Semaphore(size)


def producer(shared):
    while True:
        # production
        sleep(randint(1, 10)/10)
        # contol free space in warehouse
        shared.free.wait()
        # warehouse access
        shared.mutex.lock()
        # storage product
        sleep(randint(1, 10)/100)
        # leave warehouse
        shared.mutex.unlock()
        # increase in stocks
        shared.items.signal()


def consumer(shred):
    pass