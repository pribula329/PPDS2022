from fei.ppds import Thread, Mutex
from collections import Counter


class Shared():
    def __init__(self, size, mutex):
        self.counter = 0
        self.end = size
        self.elms = [0] * (size + 1)  # size + 1 for exception out of range
        self.mutex = mutex


def test(shared):
    while True:
        if shared.counter >= shared.end:
            break
        shared.mutex.lock()
        shared.elms[shared.counter] += 1
        shared.counter += 1
        shared.mutex.unlock()


mutex = Mutex()
shared = Shared(10000000, mutex)


t1 = Thread(test, shared)
t2 = Thread(test, shared)
t1.join()
t2.join()


print(Counter(shared.elms).most_common())
