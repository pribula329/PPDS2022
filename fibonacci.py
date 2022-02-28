from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print, Event


class SharedSemaphore:
    def __init__(self, size):
        self.fib = [0] * (size + 2)  # +2 for first and second index [0,1]
        self.fib[1] = 1
        self.object = [Semaphore(0) for x in
                       range(size + 1)]  # semaphores for thread +1 for exception out of range
        self.object[0].signal(1)


class SharedEvent:
    def __init__(self, size):
        self.fib = [0] * (size + 2)  # +2 for first and second index [0,1]
        self.fib[1] = 1
        self.object = [Event() for x in
                       range(size + 1)]  # events for thread +1 for exception out of range
        self.object[0].signal()


def fibonacci(shared, i):
    sleep(randint(1, 10) / 10)
    print("Start thread: " + str(i))
    print("Wait thread: " + str(i))
    shared.object[i].wait()
    print("Rerun thread: " + str(i))
    shared.fib[i + 2] = shared.fib[i + 1] + shared.fib[i]
    shared.object[i + 1].signal()
    print("Object send signal in thread " + str(i))


THREADS = 15
#use of semaphores
sharedSemaphores = SharedSemaphore(THREADS)
threads = [Thread(fibonacci, sharedSemaphores, i) for i in range(THREADS)]
print("------Semaphores------")
[t.join() for t in threads]

#use of events
sharedEvent = SharedEvent(THREADS)
threadsEvent = [Thread(fibonacci, sharedEvent, i) for i in range(THREADS)]
print("------Event------")
[t1.join() for t1 in threadsEvent]

print("------Semaphores------")
print(sharedSemaphores.fib)
print("------Event------")
print(sharedEvent.fib)
