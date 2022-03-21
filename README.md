# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 5

### Riešiteľ: 
> Bc. Lukáš Pribula

### Vyučujúci predmetu: 
> Mgr. Ing. Matúš Jókay, PhD.

### Zdroje: 
> Seminár PPDS 
>
> [Stránka predmetu PPDS](https://uim.fei.stuba.sk/predmet/i-ppds/)
### Verzia Pythonu
> 3.10 a 3.9

Cieľom cvičenia 5 bolo vyriešiť modifikáciu problému divochov #2.

Ako vzor sme používalí riešenie zadania Problém divochov #1, ktorá bola vysvetlena aj na seminári.

> Pri tomto zadaní išlo o riešenie, ktoré je založené na myšlienke Producentov a konzumentov. Divosi mohli jesť iba naraz 
> a až vtedy keď všetci kuchári dovaria"

> #### Pseudokód
> ````
>    class shared:
>        mutex = Mutex()
>        servings = 0
>        full_pot = Semaphore(0)
>        empty_pot = Semaphore(0)
>        barrier1 = SimpleBarrier(N)
>        barrier2 = SimpleBarrier(N)
>        cooks = 0  # cooks
>        mutexC = Mutex()
>
>
>    def get_serving_from_pot(savage_id):
>        print(info o divochovi)
>        // -1 porcia
>        servings -= 1
>        
>    def eat(savage_id):
>        print(info o divochovi)
>        // Zjedenie porcie
>        sleep(cas)  
> 
>    def savage(savage_id):
>        while True:
>            barrier1.wait()
>            barrier2.wait()
>
>            mutex.lock()
>            print()
>            if servings == 0:
>               print(budim kucharov)
>               empty_pot.signal(C) 
>               full_pot.wait()
>            get_serving_from_pot(savage_id)
>            mutex.unlock()
>            eat(savage_id)
>    
> 
>     def put_servings_in_pot(M):
>            print(info o vareni kucharov)
>            //varime určity čas
>            sleep(cas)  
>            //pridanie porcii do hrnca
>            servings += M
>            print(navarene)
>
>     def cook(M, shared, cook_id):
>           while True:
>               empty_pot.wait()
>               mutexC.lock()
>               //pridanie kuchárov
>               cooks += 1
>               
>               // kontrola či všetci kuchári su pripravený   
>               kontrola_kucharov()
>
>               // mame všetkych kuchárov
>               put_servings_in_pot(M)
>
>               // kontrola či mame dostatok porcií
>               kontrola_porcii()
>               mutexC.unlock()
>
>     //simulacia
>     def vytvorenie()
>          5 * porciu
>          3 * divoch
>          5 * kuchar
> ````