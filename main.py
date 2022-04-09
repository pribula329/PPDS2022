"""
Author: Lukáš Pribula
Simulation of the switching coprograms
"""


def coprogram1(count, fnc):
    """
    Function of simulation send workers  to count function
    :param count: count of loop
    :param fnc: next function for coprogram
    :return: yield to main function
    """
    next(fnc)
    for x in range(count):
        print("Program 1 send 1")
        fnc.send(1)
        print("Program 1 send 2")
        fnc.send(2)
        yield
    fnc.close()


def coprogram2(count, fnc):
    """
    Function of simulation send workers  to count function
    :param count: count of loop
    :param fnc: next function for coprogram
    :return: yield to main function
    """
    next(fnc)
    for x in range(count):
        print("Program 2 send 1")
        fnc.send(1)
        print("Program 2 send 2")
        fnc.send(2)
        yield
    fnc.close()


def count1():
    """
    Function for count workers
    :return: none
    """
    cnt = 0
    try:
        while True:
            cnt += (yield)
            print(f'Count of workers in count1 is {cnt}')
    except GeneratorExit:
        print(f'Coprogram 1 send {cnt} workers')


def count2():
    """
    Function for count workers
    :return: none
    """
    cnt = 0
    try:
        while True:
            cnt += (yield)
            print(f'Count of workers in count2 is {cnt}')
    except GeneratorExit:
        print(f'Coprogram 2 send {cnt} workers')


def main(c1, c2):
    """
    Function of example
    :param c1: coprogram1
    :param c2: coprogram2
    :return: none
    """
    for x in range(10):
        try:
            print()
            print(f"ETAPA {x} Program 1---------------")
            next(c1)

        except StopIteration:
            print("Program 1 is killed")
        try:
            print()
            print(f"ETAPA {x} Program 2---------------")
            next(c2)
        except StopIteration:
            print("Program 2 is killed")


cnt1 = count1()
cnt2 = count2()
main(coprogram1(1, cnt1), coprogram2(2, cnt2))
