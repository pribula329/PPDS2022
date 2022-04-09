
def coprogram1():
    print("Program 1")
    yield


def coprogram2():
    print("Program 2")
    yield


def main(c1, c2):
    while True:
        next(c1)
        next(c2)


main(coprogram1(), coprogram2())
