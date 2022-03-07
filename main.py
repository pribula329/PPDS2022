from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore, Thread, print


class Shared():
    def __init__(self, size):
        self.finished = False
        self.mutex = Mutex()
        self.items = Semaphore(0)
        self.free = Semaphore(size)
        self.count = 0


def producer(shared):
    while True:
        # production
        sleep(randint(1, 10)/10)
        print('Produce')
        # control free space in warehouse
        shared.free.wait()
        if shared.finished:
            break
        # warehouse access
        shared.mutex.lock()
        # storage product
        shared.count += 1
        # leave warehouse
        shared.mutex.unlock()
        # increase in stocks
        shared.items.signal()


def consumer(shared):
    while True:
        # stock control
        shared.items.wait()
        if shared.finished:
            break
        # warehouse access
        shared.mutex.lock()
        # get item from warehouse
        sleep(randint(1,10)/100)
        print('Get item from warehouse')
        # leave warehouse
        shared.mutex.unlock()
        # tell producent work !!!
        shared.free.signal()
        # processing item
        sleep(randint(1,10)/10)


produce_time_experiment = [0.1, 0.15, 0.25, 0.35]
produce_people_experiment = [1, 2, 3, 5, 8]
for time in produce_time_experiment:

    for person in produce_people_experiment:

        for i in range(10):

            share = Shared(10)
            producers = [Thread(producer, share) for x in range(person)]
            consumers = [Thread(consumer, share) for y in range(2)]

            sleep(0.05)
            share.finished = True
            print("Wait")
            share.items.signal(100)
            share.free.signal(100)
            for t in producers + consumers:
                t.join()
            print("End")

