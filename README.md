# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 1

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

Cieľom cvičenia 1 bolo doplniť zámky do kódu, ktorý nám bol predstavený a vysvetľovaný na seminári predmetu.

Program implementuje dve vlákna, ktoré používajú spoločný index do spoločného poľa (inicializovaný na hodnoty 0) určitej veľkosti. Každé vlákno inkrementuje ten prvok poľa, kam práve ukazuje spoločný index. Následne sa index zvýši. Ak už index ukazuje mimo poľa, vlákno svoju činnosť skončí. Po skončení vlákien sa spočíta, koľko prvkov poľa má hodnotu 1.

Pridaním zámkov do kódu sme mali predísť tomu aby sa index v poli ikrementoval viac krát a pozorovať aký má vplyv na paralelné/konkurentné programovaie.

> Program 1 (main1.py) 
````
def test(shared):
    while True:
        shared.mutex.lock()
        if shared.counter >= shared.end:
            shared.mutex.unlock()
            break
        shared.elms[shared.counter] += 1
        shared.counter += 1
        shared.mutex.unlock()
````
> Zámok sme na začiatku cyklu uzamkli a skontrolovali či sme sa nedostali mimo indexu. Následne sme inkrementovali index pola a zámok odomkli. Tým že sme použili zámok sme dosiahli že vlákna medzi sebou museli čakať
a nemohli tak inkrementovať rovnaký index poľa naraz. Jednalo sa o konkurentné vyhodnocovanie medzi vláknami.
> 
> 
> Program 2 (main2.py) 
````
def test(shared):
    shared.mutex.lock()
    while True:
        if shared.counter >= shared.end:
            shared.mutex.unlock()
            break
        shared.elms[shared.counter] += 1
        shared.counter += 1
````
> Zámok sme uzamkli pred cyklom. Skontrolovali sme či sme sa nedostali mimo indexu. Následne sme inkrementovali index pola a zámok odomkli. Tým že sme použili zámok sme dosiahli že vlákna medzi sebou museli čakať
a nemohli tak inkrementovať rovnaký index poľa naraz. V tomto prípade celý proces inkrementácie vykonalo jedno vlákno a druhé muselo čakať pokiaľ sa neinkrementovalo celé pole. Jednalo sa o konkurentné vyhodnocovanie medzi vláknami.
> 
> Program 3 (main3.py) 
````
def test(shared):
    while True:
        if shared.counter >= shared.end:
            break
        shared.mutex.lock()
        shared.elms[shared.counter] += 1
        shared.counter += 1
        shared.mutex.unlock()
````
> Pri každom cykle sme zámok uzamkli po skontrolovali či sme sa nedostali mimo indexu. Následne sme inkrementovali index pola a zámok odomkli. Tým že sme použili zámok sme dosiahli že vlákna medzi sebou museli čakať
a nemohli tak inkrementovať rovnaký index poľa naraz. Jednalo sa o konkurentné vyhodnocovanie medzi vláknami.
> Pri tomto type umiestnenia zámku sme dostavali chybu "index out of range" ktorú sme ošetrili pridanim miest do poľa

### Záver
> Použitím rôznych verzii používaných pri tomto cvičení nám odhalili chyby, ktoré by sme pri experimentovaní s jednou verziou možno nezistili. 
> Napr. pri používani pola o veľkosti 1 000 000 s verziou Python 3.10 sa nám zdalo, že kód je
> v poriadku aj keď vykonávanie programu bolo chýbné, ktoré sme zistili havne pomocou verzie Python 3.9.
> 
> Umiestňovaním zámku v programe sme zistili, že jednotlivé umiestenia majú vplyv na konkurentné/paralelné vykonávanie.
> Tým, že sme použili zámok, vlákna nám neinkrementovali index poľa viackrát. Zámok tomu zabránil a to tým, že jedno z vlakien "uspal"
> a nedovolil tak daným vláknam vykonať inkrementaciu viackrát na jednom indexe. Týmto zámok nám dopomohol ku konkurentnému/paralelnému vykonávaniu programu. 