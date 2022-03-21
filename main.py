"""
Author: Lukáš Pribula
Simulation of the example Dining savage # 2 from the subject PPDS
"""

from fei.ppds import Semaphore, Mutex, Thread, print
from random import randint
from time import sleep

"""
    M - count of serving.
    N - count of savages.
    C - count of cooks
"""
M = 5
N = 3
C = 5

class SimpleBarrier:
    """
    Implementation of barrier from subject ppds
    """

    def __init__(self, N):
        self.N = N
        self.mutex = Mutex()
        self.cnt = 0
        self.sem = Semaphore(0)

    def wait(self,
             print_str,
             savage_id,
             print_last_thread=False,
             print_each_thread=False):
        self.mutex.lock()
        self.cnt += 1
        if print_each_thread:
            print(print_str % (savage_id, self.cnt))
        if self.cnt == self.N:
            self.cnt = 0
            if print_last_thread:
                print(print_str % (savage_id))
            self.sem.signal(self.N)
        self.mutex.unlock()
        self.sem.wait()


class Shared:
    """
    Implementation of class Shared from subject ppds
    """

    def __init__(self):
        self.mutex = Mutex()
        self.servings = 0
        self.full_pot = Semaphore(0)
        self.empty_pot = Semaphore(0)
        self.barrier1 = SimpleBarrier(N)
        self.barrier2 = SimpleBarrier(N)
        self.cooks = 0  # cooks
        self.mutexC = Mutex()


def get_serving_from_pot(savage_id, shared):
    """
    Function for simulation get serving

    :param savage_id: id of savage
    :param shared: object of class Shared
    :return: none
    """
    print("divoch %2d: beriem si porciu" % savage_id)
    shared.servings -= 1


def eat(savage_id):
    """
    Function for simulation eating

    :param savage_id: id of savage
    :return: none
    """
    print("divoch %2d: hodujem" % savage_id)
    # Zjedenie porcie misionara nieco trva...
    sleep(0.2 + randint(0, 3) / 10)


def savage(savage_id, shared):
    """
    Function for simulation savage

    :param savage_id: id of savage
    :param shared: object of class Shared
    :return: none
    """
    while True:
        shared.barrier1.wait(
            "divoch %2d: prisiel som na veceru, uz nas je %2d",
            savage_id,
            print_each_thread=True)
        shared.barrier2.wait("divoch %2d: uz sme vsetci, zaciname vecerat",
                             savage_id,
                             print_last_thread=True)

        # Nasleduje klasicke riesenie problemu hodujucich divochov.
        shared.mutex.lock()
        print("divoch %2d: pocet zostavajucich porcii v hrnci je %2d" %
              (savage_id, shared.servings))
        if shared.servings == 0:
            print("divoch %2d: budim kucharov" % savage_id)
            shared.empty_pot.signal(C)
            shared.full_pot.wait()
        get_serving_from_pot(savage_id, shared)
        shared.mutex.unlock()

        eat(savage_id)


def put_servings_in_pot(M, shared):
    """
    Function for simulation put serving

    :param M: count of serving
    :param shared: object of class Shared
    :return: none
    """

    print("kuchari: varime")
    # navarenie jedla tiez cosi trva...
    sleep(0.4 + randint(0, 2) / 10)  # cooks are helping together
    shared.servings += M
    print("kuchari: navarili sme %2d porcii mozete jest" % shared.servings)


def cook(M, shared, cook_id):
    """
    Function for simulation cook

    :param cook_id: id of cook
    :param shared: object of class Shared
    :param M: count of serving
    :return: none
    """

    while True:
        shared.empty_pot.wait()
        shared.mutexC.lock()
        shared.cooks += 1
        if shared.cooks < C:
            print("kuchar %2d: idem pomahat" % cook_id)
            sleep(0.001)
        else:
            print("kuchar %2d: sme vsetci" % cook_id)
            put_servings_in_pot(M, shared)

        if shared.servings == M:
            shared.full_pot.signal()
            shared.cooks = 0
        shared.mutexC.unlock()


def init_and_run(N, M, C):
    """intit function"""
    threads = list()
    shared = Shared()
    for savage_id in range(0, N):
        threads.append(Thread(savage, savage_id, shared))
    for i in range(0, C):
        threads.append(Thread(cook, M, shared, i))

    for t in threads:
        t.join()


if __name__ == "__main__":
    init_and_run(N, M, C)