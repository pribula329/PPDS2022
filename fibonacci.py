from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print, Event


def fibonacci(i):
    sleep(randint(1, 10)/10)
    print("Start thread: " + str(i))
    print("Wait thread:" + str(i))
    semaphores[i].wait()
    print("Rerun thread: " + str(i))
    fib[i+2] = fib[i+1] + fib[i]
    semaphores[i+1].signal(1)
    print("Semaphore send signal in thread " + str(i))


THREADS = 15
fib = [0] * (THREADS+2) # +2 for first and second index [0,1]
fib[1] = 1
semaphores = [Semaphore(0) for x in range(THREADS+1)] # semaphores for thread +1 for exception out of range
semaphores[0].signal(1)
threads = [Thread(fibonacci, i) for i in range(THREADS)]

[t.join() for t in threads]

print(fib)
