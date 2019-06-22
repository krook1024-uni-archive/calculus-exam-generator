#!/usr/bin/env python3

import argparse
import ExamGenerator as eg

def main():
    q = [] # The questions-holding array
    c = {} # The category-counting dict
    n = 16 # The default number of exercises in the test

    # Command line argument handling
    parser = argparse.ArgumentParser(description='Kalkulus mintavizsga dolgozat generálása.')
    parser.add_argument('-n', type=int, dest='n', default=16, help='a kérdések száma a dolgozatban')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', help='csendes üzemmód')
    parser.add_argument('-s', '--stats', dest='stats', action='store_true', help='statisztika megjelenítése a generált dolgozatban is')
    parser.set_defaults(quiet=False, stats=False)

    args = parser.parse_args()
    n = args.n
    stats = args.stats
    quiet = args.quiet

    with open("q.txt", "r") as f:
        for line in f:
            line = line.split("|")
            category = line[0]
            question = str(line[1])
            q.append([category, question])

            # If we see a category we haven't yet, add it to
            # the list of categories.
            if category not in c:
                c[category] = 0


    gen = eg.ExamGenerator(q, n, c, quiet, stats)
    gen.gen_exam()

main()
