#!/usr/bin/env python3

import argparse
import ExamGenerator as eg

def main():
    q = [] # The questions-holding array
    c = {} # The category-counting dict
    n = 16 # The default number of exercises in the test

    # Command line argument handling
    parser = argparse.ArgumentParser(description='Generate a Calculus sample test.')
    parser.add_argument('-n', '--number', type=int, dest='n', default=16, help='the number of questions in the test')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', help='quiet mode -- don\'t print anything')
    parser.add_argument('-s', '--stats', dest='stats', action='store_true', help='show statistics in the generated test')
    parser.add_argument('-p', '--print', dest='pprint', action='store_true', help='send the generated test to the printer')
    parser.set_defaults(quiet=False, stats=False, pprint=False)

    args = parser.parse_args()
    n = args.n
    stats = args.stats
    quiet = args.quiet
    pprint = args.pprint

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


    gen = eg.ExamGenerator(q, n, c, quiet, stats, pprint)
    gen.gen_exam()

main()
