# Ovládání programu

Program interpretuje programy napsané v programovacím jazyce Brainfuck

## Popis jazyka Brainfuck
Kód brainfucku se provádí nad polem buněk, buněk je v poli 30 000 a každá buňka má kapacitu 8 bitů,
při přetečení nebo podtečení začne buňka opět od 0 nebo 255,
V jednu chvíli se pracuje pouze nad jednou(aktivní) buňkou. Kód se skládá z jednoznakových příkazů, 
všechny ostatní znaky jsou ignorovány. V Brainfucku je 8 jednoznakových příkazů:
- "+" přičtení 1 k aktivní buňce
- "-" odečtení 1 od aktivní buňky
- "<" posunutí ukazatele na buňky o 1 doleva
- ">" posunutí ukazatele na buňky o 1 doprava
- "," uložení 8 bitů ze vstupu do aktivní buňky
- "." vypsání hodnoty aktivní buňky na výstup
- "\[" začátek while loopu - pokud je hodnota aktivní buňky 0 začne interpret vykonávat příkazy za odpovídajícím znakem "\]"
- "]" konec while loopu - interpret začne vykonávat odpovídající znak "["

Soubory se zdrojovým kódem Brainfucku obyčejně končí příponou .bf

## Použití
Pro spuštění interpreteru je potřeba spustit soubor main.py, program řekne aby uživatel zadal cestu k souboru,
interpret zkusí, jestli soubor existuje, pokud ano vykoná zdrojový kód v souboru a požádá o nový soubor,
pokud soubor neexistuje interpret to uživateli oznámí a požádá o nový soubor. Pokud chce uživatel interpret ukončit,
stačí zadat místo cesty k souboru slovo exit.

Pokud je v programu příkaz pro vstup, zadává uživatel hodnotu po jednom ASCII znaku, uživatel pozná nutnost zadat znak,
pokud program vypíše: "enter a char". Interpret pracuje s hodnotami znaků zakódovaných v ASCII,
pokud program vypisuje hodnotu vypíše ji dekódovanou z ASCII.

