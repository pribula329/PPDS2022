from fei.ppds import Thread, Mutex, Semaphore, print
from random import randint


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
    print(f"You have {shared.oxygen} molecul of OXYGEN")
    print(f"You have {shared.hydrogen} molecul of HYDROGEN")


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

    shared.barrier.wait()


