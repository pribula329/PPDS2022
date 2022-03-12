from fei.ppds import Mutex, Semaphore, Thread, Event, print
from time import sleep
from random import randint


class LS:
    def __init__(self):
        self.mutex = Mutex()
        self.counter = 0

    def lock(self, semaphore):
        self.mutex.lock()
        count = self.counter
        self.counter += 1
        if self.counter == 1:
            semaphore.wait()
        self.mutex.unlock()
        return count

    def unlock(self, semaphore):
        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            semaphore.signal()
        self.mutex.unlock()


class Shared:
    def __init__(self):
        self.access_data = Semaphore(1)
        self.turnstile = Semaphore(1)
        self.monitor_LS = LS()
        self.sensor_LS = LS()
        self.valid_data = Event()


def monitor():
    pass


def sensor():
    pass
