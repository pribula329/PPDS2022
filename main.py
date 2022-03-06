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
    pass


def consumer(shred):
    pass