#!/usr/bin/env sh

for i in $(seq 1 5)
do
	python3 generate.py
done

rm -f doc/example/*.pdf
mv ./*.pdf doc/example
