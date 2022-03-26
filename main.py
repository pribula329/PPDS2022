from fei.ppds import Thread, Mutex, Semaphore, print


class Shared():
    def __init__(self):
        self.mutex = Mutex()
        self.oxygen = 0
        self.hydrogen = 0
        self.barrier = Barrier(3)
        self.oxyQueue = Semaphore(0)
        self.hydroQueue = Semaphore(0)


def oxygen():
    pass


def hydrogen():
    pass
