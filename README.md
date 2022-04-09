# Paralelné programovanie a distribuované systémy 2022
## Dokumentácia:
> Cvičenie 7

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

Cieľom cvičenia 7 bolo napísať aplikáciu, ktorá bude využívať N koprogramov a plánovač aby sme odsimulovali multasking

> Pri tomto zadaní išlo o zoznámenie sa s koprogramami a generátormi, s ktorými budeme pracovať počas 
> ďalšej časti semestra

>Zvolili sme si simuláciu posielania robotníkov do práce/stavbu
> 
> Funckia main nam zabezpečuje prepínanie medzi jednotlívymi koprogramami. 
> Comprogram posiela koprogramu count počet robotíkov, v prípade že sa ukončí posielanie
> robotníkov Comprogram zavolá metódu .close(), ktorou vypnite potrebný koprogram count.

>### Výstup programu
>![img.png](img.png)
>
> Ako možme videť na obrázku, jednotlive koprogramy sa striedaju a v prípade že ukončí svoju
> činnosť vypíče pošet robotníkov ktoré koprogram poslal

