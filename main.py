from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore, Thread, print


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
        print('Produce')
        # control free space in warehouse
        shared.free.wait()
        if shared.finished:
            break
        # warehouse access
        shared.mutex.lock()
        # storage product
        print('Storage product in warehouse')
        sleep(randint(1, 10)/100)
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
        print('Consume')
        sleep(randint(1,10)/10)


share = Shared(10)
producers = [Thread(producer, share) for x in range(5)]
consumers = [Thread(consumer, share) for y in range(2)]

sleep(1)
share.finished = True
print("Wait")
share.items.signal(100)
share.free.signal(100)
for t in producers + consumers:
        t.join()
print("End")
