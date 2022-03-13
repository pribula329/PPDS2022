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
        wait_time = randint(40, 50) / 1000

        shared.turnstile.wait()

        shared.turnstile.signal()
        monitor_count = shared.monitor_LS.lock(shared.access_data)
        print(f'monit "{mon_id}": pocet_citajucich_monitorov= {monitor_count}, trvanie_citania={wait_time}')
        sleep(wait_time)  # One update takes 40-50 ms.
        shared.monitor_LS.unlock(shared.access_data)


def sensor(shared, sen_id):
    global p
    global h
    global t
    while True:
        sleep(randint(50, 60) / 1000)  # The sensors update every 50-60 ms
        shared.turnstile.wait()
        sensor_count = shared.sensor_LS.lock(shared.access_data)
        shared.turnstile.signal()

        if sen_id == 'P cidlo':
            sensor_time = randint(10, 20) / 1000
            p = 1
        elif sen_id == 'T cidlo':
            sensor_time = randint(10, 20) / 1000
            t = 1
        else:
            sensor_time = randint(20, 25) / 1000
            h = 1

        print(f'cidlo "{sen_id}": pocet_zapisujucich_cidiel= {sensor_count}, trvanie__zapisu={sensor_time}')
        sleep(sensor_time)  # The sensor update time
        shared.sensor_LS.unlock(shared.access_data)
        if p and t and h:
            shared.valid_data.signal()
            p = 0
            t = 0
            h = 0


global p
global h
global t
p = 0
t = 0
h = 0
share = Shared()
monitors = [Thread(monitor, share, x) for x in range(8)]
sensor_P = Thread(sensor, share, 'P cidlo')
sensor_H = Thread(sensor, share, 'H cidlo')
sensor_T = Thread(sensor, share, 'T cidlo')

for m in monitors:
    m.join()
sensor_P.join()
sensor_H.join()
sensor_T.join()
