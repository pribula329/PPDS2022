from fei.ppds import Thread, Mutex, Semaphore, print


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
    shared.mutex.wait()
    shared.oxygen += 1
    if shared.hydrogen >= 2:
        shared.hydroQueue.signal(2)
        shared.hydrogen -= 2
        shared.oxyQueue.signal()
        shared.oxygen -= 1
    else:
        shared.mutex.signal()

    shared.oxyQueue.wait()

    bond() # function for print

    shared.barrier.wait()
    shared.mutex.signal()


def hydrogen(shared):
    shared.mutex.wait()
    shared.hydrogen += 1
    if shared.hydrogen >= 2 and shared.oxygen >= 1:
        shared.hydroQueue.signal(2)
        shared.hydrogen -= 2
        shared.oxyQueue.signal()
        shared.oxygen -= 1
    else:
        shared.mutex.signal()

    shared.hydroQueue.wait()

    bond()

    shared.barrier.wait()
