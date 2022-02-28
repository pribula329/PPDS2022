from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print, Event


class SharedSemaphore:
    def __init__(self, size):
        self.fib = [0] * (size + 2)  # +2 for first and second index [0,1]
        self.fib[1] = 1
        self.semaphores = [Semaphore(0) for x in
                           range(size + 1)]  # semaphores for thread +1 for exception out of range
        self.semaphores[0].signal(1)


def fibonacci(shared, i):
    sleep(randint(1, 10) / 10)
    print("Start thread: " + str(i))
    print("Wait thread:" + str(i))
    shared.semaphores[i].wait()
    print("Rerun thread: " + str(i))
    shared.fib[i + 2] = shared.fib[i + 1] + shared.fib[i]
    shared.semaphores[i + 1].signal(1)
    print("Semaphore send signal in thread " + str(i))


THREADS = 15
sharedSemaphores = SharedSemaphore(THREADS)
threads = [Thread(fibonacci, sharedSemaphores, i) for i in range(THREADS)]

[t.join() for t in threads]

print(sharedSemaphores.fib)
