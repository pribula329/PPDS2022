from fei.ppds import Thread


class Shared():
    pass


def fnc_test(shared):
    pass


shared = Shared(1_000_000)

t1 = Thread(fnc_test, shared)

t1.join()