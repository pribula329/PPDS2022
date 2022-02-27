from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print, Event


def fibonacci(i):
    fib[i+2] = fib[i+1] + fib[i]


THREADS = 10
fib = [0] * (THREADS + 2)
fib[1] = 1

threads = [Thread(fibonacci, i) for i in range(THREADS)]
[t.join() for t in threads]

print(fib)