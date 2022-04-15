"""
Author: Lukáš Pribula
Simulation of cooking synchronous
"""
from time import sleep, time


def cooking(cook):
    """
    Function of cooking
    :param cook: name of cook
    :return: none
    """
    for i in range(1, 4):
        print(f"Kuchar {cook} vari")
        sleep(i/3)
        print(f"Kuchar {cook} dovaril {i} jedlo")
        yield


def main():
    """
    Function for base simulation
    :return: none
    """
    start_time = time()
    cooks = [cooking('Lukas'), cooking('Peter'), cooking('Erik')]
    for x in range(3):
        for c in cooks:
            try:
                next(c)
            except StopIteration:
                print(f"Kuchar {c} dovaril vsetky jedla\n")
    cas = time() - start_time
    print(f"Celkovy cas varenia: {cas:.1f}")


main()
