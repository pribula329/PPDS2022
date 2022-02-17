from fei.ppds import Thread, Mutex
from collections import Counter


class Shared():
    def __init__(self, size, mutex):
        self.counter = 0
        self.end = size
        self.elms = [0] * size
        self.mutex = mutex


def test(shared):
    while True:
        shared.mutex.lock()
        if shared.counter >= shared.end:
            shared.mutex.unlock()
            break
        shared.elms[shared.counter] += 1
        shared.mutex.unlock()
        shared.counter += 1


mutex = Mutex()
shared = Shared(1000000, mutex)


t1 = Thread(test, shared)
t2 = Thread(test, shared)
t1.join()
t2.join()


print(Counter(shared.elms).most_common())