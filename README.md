# Blood Morphology Grapher

Mały skrypt wyświetlający pod postacią wykresów przebieg wyników badań morfologicznych krwi. Wizualizowane są dane otrzymywane z analizatora Pentra 2 używanego m.in. we Wrocławskim RCKiK. Pozwala to na łatwe śledzenie zmian zachodzących w składzie krwi na przestrzeni czasu. Przykład wykresu najduje się poniżej.

![Morfologia - przykład](https://i.imgur.com/bj7rkjE.png)

Wizualizowane dane:
* **RBC** *[mln/µl]* - Ilość czerwonych krwinek (erytrocytów)
* **HGB** *[g/dl]* - Ilość hemoglobiny w ogólnej masie erytrocytów
* **HCT** *[%]* - Hematokryt - procentowa objętość erytrocytów we krwi
* **MCV** *[fl]* - Średnia objętość erytrocytu
* **MCH** *[pg]* - Stężenie hemoglobiny w erytrocycie
* **MCHC** *[g/dl]* - Stężenie hemoglobiny w ogólnej masie erytrocytów
* **RDW** *[%]* - Anizocytoza erytrocytów - rozpiętość rozkładu objętości erytrocytów
* **PLT** *[tys/µl]* - Ilość płytek krwi (trombocytów)
* **PDW** *[%]* - Anizocytoza trombocytów - rozpiętość rozkładu objętości trombocytów
* **MPV** *[fl]* - Średnia objętość trombocytu
* **WBC** *[tys/µl]* - Ilość białych krwinek (leukocytów)
* **PCT** *[%]* - Poziom prokalcytoniny (białka tarczycy) w osoczu krwi

Dane wejściowe pobierane są z pliku *data.csv* który powinien znajdować się obok modułu wykonywalnego. Jego przykładowa struktura:

```
dates;RBC;HGB;HCT;MCV;MCH;MCHC;RDW;PLT;PDW;MPV;WBC;PCT
18.12.17;5.04;13.0;39.7;79;25.9;32.8;17.4;220;18.0;9.5;3.8;0.2
05.02.18;5.58;15.4;47.0;84;27.6;32.8;18.4;230;18.8;9.5;4.6;0.2
04.04.18;5.08;15.4;46.1;91;30.2;33.3;14.5;206;18.0;9.3;5.1;0.2
06.06.18;4.96;15.5;45.5;92;31.3;34.1;13.6;180;17.8;9.2;4.3;0.2
```
