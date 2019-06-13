#!/usr/bin/env bash

cdir="."

gen_example() {
	for i in $(seq 1 5)
	do
		python3 $cdir/generate.py
	done
}

delete_examples() {
	rm -f $cdir/doc/example/*.pdf
}

move_examples() {
	mv $cdir/*.pdf $cdir/doc/example
}

# Amennyiben az util mappából hívjuk a szkriptet, úgy a szülő mappába szükséges átlépnünk a futtatás előtt.
[[ "$PWD" =~ util ]] && cd ".."

gen_example
delete_examples
move_examples
