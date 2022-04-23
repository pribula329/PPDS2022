# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 9

### Riešiteľ: 
> Bc. Lukáš Pribula

### Vyučujúci predmetu: 
> Mgr. Ing. Matúš Jókay, PhD.

### Zdroje: 
> Seminár PPDS 
>
> [Stránka predmetu PPDS](https://uim.fei.stuba.sk/predmet/i-ppds/)
>
> [Kaggle - numba cuda](https://www.kaggle.com/code/landlord/numba-cuda-mandelbrot/notebook)

### Verzia Pythonu
> 3.10 a 3.9

Cieľom cvičenia 9 bolo napísať aplikáciu, ktorá pracuje pomocou GPU.
>Zvolili sme si zrkadlovú transformáciu obrázka.

> ### Program
> Program(main.py) načíta obrázok a vytvorí zrkadlovú transformáciu.
> Premenná **threadsperblock** predstavuje počet vlákien v bloku,**blockspergrid**
> počet vlákien v mriežke.
> Funkcia rotuj nám zrkadlovo obráti obrázok

> ### Výsledok
>![original](mini.png) ![vysledok](out.png)
>