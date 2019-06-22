# 🤓 kalkulus-vizsga-gyak

A `kalkulus-vizsga-gyak` egy egyszerű Python program ami egy megadott
kérdéssorból véletlenszerűen állít össze egy Kalkulus vizsgadolgozatot.
Jelenleg **több mint 110** kérdést tárol, melyek egy része már szerepelt
vizsgadolgozatban a 2018/9-es tanév során, a másik része pedig nagy
valószínűséggel szerepelhet.

A program igyekszik a valódi vizsgadolgozatokhoz vizuálisan minél jobban
hasonlítani, ezzel is azt az érzést keltve a felhasználóban, hogy vizsgán vesz
részt éppen. A generált dolgozatokat ajánlatos kinyomtatni, és tollal,
ceruzával kitölteni, hogy a valódi vizsgán minél sikeresebbek lehessünk.

A mintadolgozatok generálása a [LaTeX](https://en.wikipedia.org/wiki/LaTeX)
typesetting nyelven alapszik, ezáltal futtatásához **pdflatex** telepítése
szükséges! Ez a legtöbb GNU/Linux disztribúció alatt egyszerűen megtehető,
viszont léteznek Windows-binárisok is.

## Példák

A [doc/example](doc/example) mappában található néhány példa.

## Használat

```
➜ ./generate.py -h
usage: generate.py [-h] [-n N] [-q] [-s]

Generate a Calculus sample test.

optional arguments:
  -h, --help        show this help message and exit
  -n N, --number N  the number of questions in the test
  -q, --quiet       quiet mode -- don't print anything
  -s, --stats       show statistics in the generated test
```
