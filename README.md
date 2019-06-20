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
# python3 generate.py [opcionális: kérdések száma a dolgozatban]
```
