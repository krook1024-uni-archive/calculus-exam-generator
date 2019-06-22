#!/usr/bin/env bash

gen_example() {
	for i in $(seq 1 5)
	do
		python3 ./generate.py
	done
}

delete_examples() {
	rm -f ./doc/example/*.pdf
}

move_examples() {
	mv ./*.pdf ./doc/example
}

rename_examples() {
	i=1
	workdir=./doc/example
	for f in `ls $workdir`; do
		mv $workdir/$f $workdir/$i.pdf
		i=$(($i+1))
	done
}

# Amennyiben az util mappából hívjuk a szkriptet, úgy a szülő mappába szükséges átlépnünk a futtatás előtt.
[[ "$PWD" =~ util ]] && cd ".."

gen_example
delete_examples
move_examples
rename_examples
