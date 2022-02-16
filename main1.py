from fei.ppds import Thread
from collections import Counter

class Shared():
    def __init__(self,size):
        self.counter = 0
        self.end = size
        self.elms = [0] * size


def test(shared):
    while shared.counter < shared.end:
        shared.elms[shared.counter] += 1
        shared.counter += 1


shared = Shared(10000000)

t1 = Thread(test, shared)
t2 = Thread(test, shared)
t1.join()
t2.join()

print(Counter(shared.elms).most_common())