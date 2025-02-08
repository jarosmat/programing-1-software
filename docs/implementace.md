# Implementace interpreteru

Program implementuji ve 3 souborech:
1. Utilities, implementuje třídy:
   1. Node
   2. NodeArray
   3. Pointer
2. operations, implementuje třídy
   1. MultiOperation, od které dědí třídy:
      1. Addition
      2. Subtraction
      3. ShiftLeft
      4. ShiftRight
   2. Task, od které dědí třída:
      1. MainTask
   3. Printer
   4. Inputer
   5. SetNodeZero
   6. MoveData
3. preproccesor, implementuje funkce:
   1. parser
   2. resolve_loop
   3. create_instance
## Pole buněk

Pole buněk je reprezentováno instancí třídy NodeArray, jednotlivé buňky jsou reprezentovány instancemi třídy Node,
ukazatel na aktivní buňku je reprezentován instancí třídy Pointer. Instance třídy Pointer při vykonávání programu 
zprostředkovává jednotlivé buňky, které si vždy vyžádá od instace třídy NodeArray. Tato instance třídy Pointer se 
stará také o udržování hodnoty samotného ukazatele do pole buněk.

## Vyhodnocování zdrojového kódu

Interpret napřed projde celý zdrojový kód a upraví si ho do lepší podoby (vytvoří si instance tříd pro jednotlivé operace)
a následně vykoná tento mezikód

### První průchod

První průchod provádí funkce parser. 
Jednotlivé cykly jsou uzavřené do instancí Třídy Task, celý program v brainfucku je uzavřen v instanci třídy MainTask.
Elementární příkazy jsou uloženy do instancí tříd následovně:

- "+" třída Addition
- "-" třída Subtraction
- "<" třída ShiftLeft
- ">" třída ShiftRight
- "," třída Inputer
- "." třída Printer

Navíc jedna instance tříd Addition, Subtraction, ShiftLeft, ShiftRight reprezentuje vždy tolik daných příkazů,
kolik se jich vyskytuje bezprostředně za sebou

Funkce parser ví o každém cyklu, jestli je v něm další cyklus vnořený a pokud není, předá daný cyklus funkci resolve loop,
která může z cyklu vytvořit instanci jedné z těchto tříd, pokud jedné z nich vyhovuje:

#### Třída SetNodeZero

Pokud se v cyklu vyskytuje pouze instance jedné třídy a to buď třídy Addition nebo Subtraction, tak je cyklus nahrazen
instancí třídy SetNodeZero.
Instance této třídy nastaví hodnotu aktivní buňky na 0.

#### Třída MoveData

Pokud se v cyklu vyskytují právě 4 operace a to v tomto pořadí:

1. Subtraction - reprezentující pouze jeden příkaz "-"
2. ShiftLeft nebo ShiftRight
3. Addition nebo Subtracton - reprezentující libovolný počet příkazů "+" nebo "-"
4. Pokud 2. byla instance ShiftLeft, musí být toto instance ShiftRight, pokud 2. byla instance ShiftRight musí být toto instance ShiftLeft

Navíc 2. a 4. objekt musí reprezentovat stejný počet opačných posunů. Pokud je toto splněno je cyklus nahrazen instancí 
této třídy.
Instance této třídy vynuluje aktivní buňku a její hodnotu vynásobenou tím, kolik příkazů reprezentuje 3. objekt přičte
nebo odečte (podle toho instance které třídy je 3. objekt) k aktivní buňce po posunutí ukazatele podle 2. objektu.
Nakonec posune ukazatel zpět na původní buňku.



### Druhý průchod

Funkce parser vrátí instanci třídy MainTask, ve které jsou uloženy všechny ostatní operace, každá Třída v souboru operations
implementuje metodu execute, které vykoná danou operaci. Takže jako poslední Interpreter spustí metodu execute na objekt 
vrácený funkcí parser, která na každý objekt přímo uložený v tomto objektu zavolá jeho metodu execute, pokud je tento objekt
instance třídy Task, je funkce execute volaná rekurzivně, dokud se cyklus nedostane na elementární operace
