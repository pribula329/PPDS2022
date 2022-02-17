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
> 3.10

Cieľom cvičenia 1 bolo doplniť zámky do kódu, ktorý nám bol predstavený a vysvetľovaný na seminári predmetu.

Program implementuje dve vlákna, ktoré používajú spoločný index do spoločného poľa (inicializovaný na hodnoty 0) určitej veľkosti. Každé vlákno inkrementuje ten prvok poľa, kam práve ukazuje spoločný index. Následne sa index zvýši. Ak už index ukazuje mimo poľa, vlákno svoju činnosť skončí. Po skončení vlákien sa spočíta, koľko prvkov poľa má hodnotu 1.

Pridaním zámkov do kódu sme mali predísť tomu aby sa index v poli ikrementoval viac krát.
