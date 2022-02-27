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
    """ Function for print Thread on rendezvous

    :param thread_name: Name of Thread (id)
    :return: none
    """
    sleep(randint(1, 10)/10)
    print('rendezvous: %s' % thread_name)


def ko(thread_name):
    """ Function for print Thread after barrier

        :param thread_name: Name of Thread (id)
        :return: none
        """
    print('ko: %s' % thread_name)
    sleep(randint(1, 10)/10)


def barrier_example(barrier1, barrier2, thread_id):
    """ Example how work barrier

    :param barrier1: First barrier of class SimpleBarrier
    :param barrier2: Second barrier of class SimpleBarrier
    :param thread_id: id of Thread
    :return: None
    """
    while True:
        rendezvous(thread_id)
        barrier1.wait()
        ko(thread_id)
        barrier2.wait()


sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)

threads = [Thread(barrier_example, sb1, sb2, i) for i in range(5)]
[t.join() for t in threads]
