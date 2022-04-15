from time import sleep,time


def cooking(cook):
    for i in range(1,4):
        print(f"Kuchar {cook} vari")
        sleep(i/3)
        print(f"Kuchar {cook} dovaril {i} jedlo")
        yield


def main():
    start_time = time()
    cooks = ['Lukas', 'Peter', 'Erik']

    for c in cooks:
        cook = cooking(c)
        for x in range(4):
            try:
                next(cook)
            except StopIteration:
                print(f"Kuchar {c} dovaril vsetky jedla\n")
    cas = time() - start_time
    print(f"Celkovy cas varenia: {cas:.1f}")

main()