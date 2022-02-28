# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 2

### Riešiteľ: 
> Bc. Lukáš Pribula

### Vyučujúci predmetu: 
> Mgr. Ing. Matúš Jókay, PhD.

### Zdroje: 
> Seminár PPDS 
> 
>https://greenteapress.com/wp/semaphores/
> 
> [Stránka predmetu PPDS](https://uim.fei.stuba.sk/predmet/i-ppds/)
### Verzia Pythonu
> 3.10 a 3.9
### Obsah
Cieľom cvičenia 2 bolo implementovať/modifikovať dva úlohy/programy, ktoré boli predstavené na seminári predmetu PPDS.

> **Program 1 (barrier.py)**

>Cieľom prvej úlohy bolo modifikovať barrieru pomocou udalosti Event(). 
Prv sme pracovali s triedou, ktorá sa nachádza nižšie
````
class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.N:
            self.counter = 0
            self.event.set()
        self.mutex.unlock()
        self.event.wait()
````
>Zmenili sme teda implementáciu triedy SimpleBarrier. Metódu **Semaphore()** sme nahradili metodou **Event()**
z modulu fei.ppds. V danej triede bariery sme následne upravili funkciu **wait()**. Pomocou tejto triedy
a jej funkcie wait() sme zabezpečili aby jednotlivé vlákna na seba čakali. 

>Konkrétne pomocou **event.wait()**, ktorý zabezpečoval aby vlákna čakali pokiaľ nenastane udalosť (**event.set()**)
Potom ako nastala udalosť sa vlákna odblokovali a pokračovali vo vykonávaní kódu. 

>Nakoľko sme pri experimentovaní zistili že korektné vykonávanie vlákien nastane iba pri prvotnom cykle, 
bolo potrebné ďalej upraviť kód programu. Aby sme zabezepečili znovupoužiteľnosť udalosti, bolo 
potrebné „vynulovať“ nastavenie udalosti pomocou metódy **clear()**. Po jej zavolaní začali
byť znovu všetky volania **wait()** blokujúce, až pokiaľ nebolo nad týmto objektom (znovu) vyvolaná metóda **set()**.
````
class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.mutex.lock()
        if self.counter == 0:
            self.event.clear()
        self.counter += 1
        if self.counter == self.N:
            self.counter = 0
            self.event.set()
        self.mutex.unlock()
        self.event.wait()

````
>Týmto sme zabezpečili aby vykonávanie barrieri pomocou udalosti bolo korektné aj pri používaní v cykle.
 

> **Program 2 (fibonacci.py)**

>Cieľom druhej úlohy bolo navrhnúť výpočet fibonacciho postupnosti pomocou
> synchronizačných nástrojov. Prv sme pracovali so semaformi a neskôr sme 
> riešenie upravili aj pre udalosti. 
````
class SharedSemaphore:
    """
    Class for Semaphore
    """
    def __init__(self, size):
        self.fib = [0] * (size + 2)  # +2 for first and second index [0,1]
        self.fib[1] = 1
        self.object = [Semaphore(0) for x in
                       range(size + 1)]  # semaphores for thread +1 for exception out of range
        self.object[0].signal(1)


class SharedEvent:
    """
        Class for Event
    """
    def __init__(self, size):
        self.fib = [0] * (size + 2)  # +2 for first and second index [0,1]
        self.fib[1] = 1
        self.object = [Event() for x in
                       range(size + 1)]  # events for thread +1 for exception out of range
        self.object[0].signal()
````
>Jednotlive triedy obsahujú inicializaciu poľa pre ukladanie hodnôt fibonacciho
> postupnosti a inicializaciu jednotlivých synchronizačných objektov.

>Po vytvorení vlákien a zavolaní funkcie na výpočet sme donutili vlákna čakať
> pomocou synchronizačných nástrojov ( **shared.object[i].wait()** ),dokiaľ
> nedostanú signal aby mohli pokračovať ďalej, okrem prvého vlákna
> ktorému sme už pri inicializacii vytvorili signal aby mohol pokračovať ďalej.
> Postupne takto každé vlákno (serializovane), bolo odblokovane ( **shared.object[i].signal()** )
> pomocou synchronizačných nástrojov (semafór a udalosť) a pokračovalo vo vykonávaní výpočtu.
````
def fibonacci(shared, i):
    """
    Function for calculate fibonacci sequence with Threads.

    :param shared: shared object of fibonacci array and
                   array of synchronization objects for threads
    :param i: id of thread
    :return: none
    """
    sleep(randint(1, 10) / 10)
    print("Start thread: " + str(i))
    print("Wait thread: " + str(i))
    shared.object[i].wait()
    print("Rerun thread: " + str(i))
    shared.fib[i + 2] = shared.fib[i + 1] + shared.fib[i]
    shared.object[i + 1].signal()
    print("Object send signal in thread " + str(i))

````
> Na vyriešenie tejto úlohy bolo potrebné vytvoriť N+1 synchronizačných objektov
> aby každe z vlákien dostalo od synchronizačného objektu signál, aby pokračovalo ďalej.