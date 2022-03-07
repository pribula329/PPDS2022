from random import randint
from time import sleep
from matplotlib import pyplot
from fei.ppds import Mutex, Semaphore, Thread, print


class Shared():
    def __init__(self, size):
        self.finished = False
        self.mutex = Mutex()
        self.items = Semaphore(0)
        self.free = Semaphore(size)
        self.count = 0


def producer(shared):
    while True:
        # production
        sleep(randint(1, 10)/100)
        #print('Produce')
        # control free space in warehouse
        shared.free.wait()
        if shared.finished:
            break
        # warehouse access
        shared.mutex.lock()
        # storage product
        shared.count += 1
        # leave warehouse
        shared.mutex.unlock()
        # increase in stocks
        shared.items.signal()




def consumer(shared):
    while True:
        # stock control
        shared.items.wait()
        if shared.finished:
            break
        # warehouse access
        shared.mutex.lock()
        # get item from warehouse
        sleep(randint(1,10)/1000)
        #print('Get item from warehouse')
        # leave warehouse
        shared.mutex.unlock()
        # tell producent work !!!
        shared.free.signal()




produce_time_experiment = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
produce_people_experiment = [1, 2, 3, 5, 8, 10]
result_experiment = []
for time in produce_time_experiment:

    for person in produce_people_experiment:
        sum_person = 0
        for i in range(10):

            share = Shared(10)
            producers = [Thread(producer, share) for x in range(person)]
            consumers = [Thread(consumer, share) for y in range(10)]

            sleep(0.1)
            share.finished = True
            share.items.signal(100)
            share.free.signal(100)
            for t in producers + consumers:
                t.join()
            #print("---------------")
            item_sec = share.count / 0.1
            sum_person += item_sec
        print(person)
        result_experiment.append((time, person, sum_person / 10))
    print(time)


fig = pyplot.figure()
ax = pyplot.axes(projection="3d")
x = [k[0] for k in result_experiment]
y = [k[1] for k in result_experiment]
z = [k[2] for k in result_experiment]

ax.set_xlabel("Time production")
ax.set_ylabel("Count producers")
ax.set_zlabel("Count product for seconds")

ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

pyplot.show()
