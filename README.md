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
