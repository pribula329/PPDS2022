from fei.ppds import Thread, Mutex, Semaphore, print
from random import randint
from time import sleep

class Barrier():
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.turnstile = Semaphore(0)

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.N:
            self.counter = 0
            self.turnstile.signal(self.N)
        self.mutex.unlock()
        self.turnstile.wait()


class Shared():
    def __init__(self):
        self.mutex = Mutex()
        self.oxygen = 0
        self.hydrogen = 0
        self.barrier = Barrier(3)
        self.oxyQueue = Semaphore(0)
        self.hydroQueue = Semaphore(0)


def bond(shared):
    print("A H2O molecule is formed")
    sleep(0.001)
    print("A H2O molecule was created")
    print(f"You have {shared.oxygen} molecul of OXYGEN")
    print(f"You have {shared.hydrogen} molecul of HYDROGEN")
    print("----------------------------")


def oxygen(shared):
    shared.mutex.lock()
    shared.oxygen += 1
    print(f"You have {shared.oxygen} molecul of OXYGEN")
    if shared.hydrogen >= 2:
        shared.hydroQueue.signal(2)
        shared.hydrogen -= 2
        shared.oxyQueue.signal()
        shared.oxygen -= 1
    else:
        shared.mutex.unlock()

    shared.oxyQueue.wait()

    bond(shared) # function for print
    sleep(0.5)
    shared.barrier.wait()
    shared.mutex.unlock()


def hydrogen(shared):
    shared.mutex.lock()
    shared.hydrogen += 1
    print(f"You have {shared.hydrogen} molecul of HYDROGEN")
    if shared.hydrogen >= 2 and shared.oxygen >= 1:
        shared.hydroQueue.signal(2)
        shared.hydrogen -= 2
        shared.oxyQueue.signal()
        shared.oxygen -= 1
    else:
        shared.mutex.unlock()

    shared.hydroQueue.wait()

    bond(shared)
    sleep(0.5)

    shared.barrier.wait()

thread = []
shared = Shared()
for x in range(0,10):
    typ = randint(1,2)
    if typ == 1:
        tH = Thread(hydrogen,shared)
        thread.append(tH)
    else:
        tO = Thread(oxygen, shared)
        thread.append(tO)


for t in thread:
    t.join()

