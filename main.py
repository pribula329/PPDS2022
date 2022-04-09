def coprogram1(count):
    for x in range(count):
        print("Program 2 start 1")
        yield
        print("Program 2 start 2")
        yield
        print("Program 2 start 3")
        yield


def coprogram2(count):
    for x in range(count):
        print("Program 2 start 1")
        yield
        print("Program 2 start 2")
        yield
        print("Program 2 start 3")
        yield

def count1():
    cnt = 0
    try:
        while True:
            cnt += (yield)
    except GeneratorExit:
        print(f'Coprogram 1 send {cnt} employer')

def main(c1, c2):
    for x in range(10):
        try:
            next(c1)
        except StopIteration:
            print("Program 1 is killed")
        try:
            next(c2)
        except StopIteration:
            print("Program 2 is killed")


main(coprogram1(1), coprogram2(3))
