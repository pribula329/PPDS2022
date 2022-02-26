from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print


class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        # ...

    def wait(self):
        # ...
        pass


def barrier_example(barrier, thread_id):
    sleep(randint(1, 10) / 10)
    print("thread %d before barrier" % thread_id)
    barrier.wait()
    print("thread %d after barrier" % thread_id)


sb = SimpleBarrier(5)

