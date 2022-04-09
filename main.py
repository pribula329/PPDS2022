"""
Author: Lukáš Pribula
Simulation of the switching coprograms
"""


def coprogram1(count, fnc):
    """
    Function of simulation send employer  to count function
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
    Function of simulation send employer  to count function
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
    Function for count employer
    :return: none
    """
    cnt = 0
    try:
        while True:
            cnt += (yield)
            print(f'Count of employer in count1 is {cnt}')
    except GeneratorExit:
        print(f'Coprogram 1 send {cnt} employer')


def count2():
    """
    Function for count employer
    :return: none
    """
    cnt = 0
    try:
        while True:
            cnt += (yield)
            print(f'Count of employer in count2 is {cnt}')
    except GeneratorExit:
        print(f'Coprogram 2 send {cnt} employer')


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
            print()
            print("Program 1 is killed")
        try:
            print()
            print(f"ETAPA {x} Program 2---------------")
            next(c2)
        except StopIteration:
            print()
            print("Program 2 is killed")


cnt1 = count1()
cnt2 = count2()
main(coprogram1(3, cnt1), coprogram2(5, cnt2))
