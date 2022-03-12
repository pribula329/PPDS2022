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


def monitor(shared, mon_id):
    shared.valid_data.wait()
    while True:
        wait_time = randint(40, 50)/1000
        sleep(wait_time)  # One update takes 40-50 ms.
        shared.turnstile.wait()
        monitor_count = shared.monitor_LS.lock(shared.access_data)
        shared.turnstile.signal()

        print(f'monit "{mon_id}": pocet_citajucich_monitorov= {monitor_count}, trvanie_citania={wait_time}')
        shared.monitor_LS.unlock(shared.access_data)


def sensor():
    pass
