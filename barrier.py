from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print, Event


class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.mutex.lock()
        if self.counter == 0:
            self.event.clear()
        self.counter += 1
        if self.counter == self.N:
            self.counter = 0
            self.event.set()
        self.mutex.unlock()
        self.event.wait()


def rendezvous(thread_name):
    sleep(randint(1, 10)/10)
    print('rendezvous: %s' % thread_name)


def ko(thread_name):
    print('ko: %s' % thread_name)
    sleep(randint(1, 10)/10)


def barrier_example(barrier1, barrier2, thread_id):
    while True:
        rendezvous(thread_id)
        barrier1.wait()
        ko(thread_id)
        barrier2.wait()


sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)

threads = [Thread(barrier_example, sb1, sb2, i) for i in range(5)]
[t.join() for t in threads]
