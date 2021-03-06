# Blood Morphology Grapher

### Opis

Mały skrypt wyświetlający pod postacią wykresów przebieg wyników badań morfologicznych krwi. Wizualizowane są dane otrzymywane z analizatora Pentra 2 używanego m.in. we Wrocławskim RCKiK. Pozwala to na łatwe śledzenie zmian zachodzących w składzie krwi na przestrzeni czasu. Ukazywane są także wartości brzegowe względem stosunkowego mężczyzny lub kobiety aby widzieć czy wartości nie oscylują przy zalecanych granicach. Przykład wykresu najduje się poniżej.

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
* **LYM** *[%]* - Procentowy udział limfocytów w leukocytach
* **MON** *[%]* - Procentowy udział monocytów w leukocytach
* **NEU** *[%]* - Procentowy udział neutrofili w leukocytach
* **BAS** *[%]* - Procentowy udział bazofili w leukocytach
* **EOS** *[%]* - Procentowy udział eozynofili w leukocytach
* **LYM** *[tys/µl]* - Ilościowy udział limfocytów w leukocytach
* **MON** *[tys/µl]* - Ilościowy udział monocytów w leukocytach
* **NEU** *[tys/µl]* - Ilościowy udział neutrofili w leukocytach
* **BAS** *[tys/µl]* - Ilościowy udział bazofili w leukocytach
* **EOS** *[tys/µl]* - Ilościowy udział eozynofili w leukocytach
* **ALY** *[%]* - Procent limfocytów atypowych (reaktywnych)
* **ALY** *[tys/µl]* - Ilość limfocytów atypowych (reaktywnych)
* **LIC** *[tys/µl]* - Ilość dużych niedojrzałych komórek (limfoblastów)

Po uruchomieniu programu wygenerowane wykresy zostaną automatycznie zapisane do folderu z modułem wykonywalnym.

### Uruchomienie

Skrypt uruchamia się przy pomocy Pythona w wersji co najmniej 3.3 odpalając plik wykonywalny:
```
py -3 main.py
```

Możliwe są dodatkowe przełączniki:

* `-f <sciezka/plik.csv>` zmiana lokacji pliku *.csv* z danymi
* `-s` pokazywanie wykresów od razu po ich utworzeniu bez zapisywania ich
* `-k` rysowanie wartości brzegowych dla statystycznej kobiety zamiast mężczyzny

### Dane wejściowe

Dane wejściowe pobierane są domyślnie z pliku *data.csv* który powinien znajdować się obok modułu wykonywalnego. Jego przykładowa struktura:

```
date;RBC;HGB;HCT;MCV;MCH;MCHC;RDW;PLT;PDW;MPV;WBC;PCT;LYM%;MON%;NEU%;BAS%;EOS%;LYM;MON;NEU;BAS;EOS;ALY;ALY%;LIC
18.12.17;5.04;13.0;39.7;79;25.9;32.8;17.4;220;18.0;9.5;3.8;0.2;12.5;6.5;72.3;0.5;2.2;1.68;0.7;8.5;0.08;0.25;0.17;1.3;0.12
05.02.18;5.58;15.4;47.0;84;27.6;32.8;18.4;230;18.8;9.5;4.6;0.2;13.1;6.2;74.6;0.4;1.9;1.84;0.9;8.9;0.12;0.31;0.15;1.5;0.14
04.04.18;5.08;15.4;46.1;91;30.2;33.3;14.5;206;18.0;9.3;5.1;0.2;13.8;5.7;73.2;0.4;1.7;1.24;0.6;9.2;0.11;0.29;0.15;1.4;0.14
06.06.18;4.96;15.5;45.5;92;31.3;34.1;13.6;180;17.8;9.2;4.3;0.2;14.2;6.1;76.5;0.3;2.0;1.53;0.6;8.4;0.14;0.29;0.15;1.5;0.16
```

Plik ten można utworzyć ręcznie bądź wykorzystać kreator do dodawania próbek z badań. W tym celu należy uruchomić:
```
py -3 creator.py
```

Okno kreatora do wpisywania wyników badań:

![Okno kreatora](https://i.imgur.com/uUzBuGs.png)

Po wciśnięciu *Add data to CSV* wpisane dane zostaną dodane do aktualnie wybranego pliku *.csv*. Plik ten zostanie stworzony automatycznie jeśli nie istnieje.

Dodatkowe opcje kreatora:
* *File -> Choose other input CSV file* - okno zmiany pliku *.csv* do zapisywania danych
* *File -> Choose parsed OCR file to fill data* - okno wybrania pliku tekstowego z dowolnego oprogramowania OCR po przetworzeniu zdjęcia/skanu kartki z wynikami; te dane, które uda się odczytać zostaną automatycznie wypełnione w kreatorze
