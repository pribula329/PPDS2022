from time import sleep


def cooking(cook):
    for i in range(3):
        print(f"Kuchar {cook} vari")
        sleep(i/10)
        print(f"Kuchar {cook} dovaril {i} jedlo")
        yield


def main():
    pass
