#!/usr/bin/env sh

sort < ../q.txt | uniq > tmp.txt
rm -f '../q.txt'
mv tmp.txt ../q.txt
rm -f tmp.txt
