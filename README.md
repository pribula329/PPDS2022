# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 6

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

Cieľom cvičenia 6 bolo vyriešiť jeden z daných problémov, ktoré nám boli predstavene na predmete PPDS

Vybrali sme si tvorenie molekul vody

> Pri tomto zadaní išlo o synchronizačný problém, pri ktorom bolo potrebné spojiť potrebný počet daných molekul kyslíka 
> a vodíka dokopy.

>Pre tento problem bolo potrebné použiť barieru, aby každé vlákno(kyslík alebo vodík) čakalo, pokiaľ sa
z daných vlakien nebude dať vytvoriť molekula H2O.
>Taktiež bolo potrebné použiť mutex a semafor. Semafor nám zabezpečil čakanie vlákien, čiže pridával
> dané vlákna do "zásobnika". Mutex zabezpečoval korektnosť počítadiel.