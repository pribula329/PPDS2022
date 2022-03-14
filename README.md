# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 4

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

Cieľom cvičenia 4 bolo vyriešiť zadanie Atomová elektráreň #2.

Ako vzor sme používalí riešenie zadania Atomová elektráreň #1, ktorá bola vysvetlena aj na seminári.

> Pri tomto zadaní išlo o vzájomne vylúčenie kategorií(monitory a senzory). Monitori mohli iba čitať informácie od 
> senzorov a senzori iba zapisovať údaje. Pri implementácií sme použili vzor zo semináru (Atomová elektráreň #1), pri 
> ktorom bole potrebné spraviť určité úpravy pre toto zadanie. Použili sme LightSwitch, Event a Semafor. Event nám pomohol aby monitori čítali 
> údaje až potom čo vykonajú aktualizáciu všetky senzori. LightSwitch a Semafor nám zabezpečili aby jednotlive kategórie(monitory a senzory) medzi 
> sebou spolupracovali a "nebili sa navzajom"

> #### Pseudokód
> ````
>    class shared:
>        access_data = Semaphore(1)
>        turnstile = Semaphore(1)
>        monitor_LS = LightSwitch()
>        sensor_LS = LightSwitch()
>        valid_data = Event()
>
>
>    def monitor(mon_id):
>        //monitor musi čakať na senzori
>        valid_data.wait()
>        
>        while True:
>            
>            // monitory prechádzajú cez turniket, pokým ho nezamkne senzor
>            turnstile.wait()
>            turnstile.signal()
>            
>            // získnie prístupu k úložisku
>            monitor_count = monitor_LS.lock(access_data)
>            //pristup k udajom
>            print(info o monitoroch)
>             
>            // čas čitania
>            sleep(40 - 50 ms)
>                
>            // prečítali sme údaje, odchádzame z úložiska
>            monitor_LS.unlock(access_data)
>    
>    
>    def sensor(shared, sen_id):
>        while True:
>            // update sensorov
>            sleep(50 - 60 ms)
>            
>            // zablokujeme turniket, aby senzori mohli pracovať
>            turnstile.wait()
>            // získnie prístupu k úložisku
>            sensor_count = sensor_LS.lock(access_data)
>            turnstile.signal()
>            
>            //pristup k udajom
>            print(info o senzoroch)
>            
>            // čas zapisovania
>            sleep(podľa typu senzora)  
>            
>            // prečítali sme údaje, odchádzame z úložiska
>            sensor_LS.unlock(access_data)
>            
>            konrola všetkých senzorov:
>                // signalizacia pre pokračovanie
>                valid_data.signal()
>    
>    //simulacia
>    def vytvorenie()
>       8 * monitor
>       1 * P senzor
>       1 * H senzor
>       1 * T senzor
> ````
