#!/usr/bin/env python3

import argparse
import ExamGenerator as eg

def main():
    q = []  # The questions-holding array
    c = {}  # The category-counting dictionary

    # Command line argument handling
    parser = argparse.ArgumentParser(description='Generate a Calculus sample test.')
    parser.add_argument('-n', '--number', type=int, dest='n', default=16,
            help='the number of questions in the test')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true',
            help='quiet mode -- don\'t print anything')
    parser.add_argument('-s', '--stats', dest='stats', action='store_true',
            help='show statistics in the generated test')
    parser.add_argument('-p', '--print', dest='pprint', action='store_true',
            help='send the generated test to the printer')
    parser.add_argument('-H', '--hard', dest='hard', action='store_true',
            help='only include "harder" questions')
    parser.set_defaults(n=16, quiet=False, stats=False, pprint=False,
            hard=False)

    args = parser.parse_args()
    n = args.n              # The number of exercises in a test
    stats = args.stats      # Show statistics or don't
    quiet = args.quiet      # Print messages or don't
    pprint = args.pprint    # Print the generated exam or don't
    hard = args.hard        # Hard-mode

    # Read the questions from q.txt

    filename = "q.txt"

    if hard:
        filename = "q_hard.txt"

    with open(filename, "r") as f:
        for line in f:
            line = line.split("|")
            category = line[0]
            question = str(line[1])
            q.append([category, question])

            # If we see a category we haven't yet, add it to
            # the list of categories.
            if category not in c:
                c[category] = 0

    # Initialize the exam generator class
    gen = eg.ExamGenerator(q, n, c, quiet, stats, pprint)
    gen.gen_exam()

if __name__ == '__main__':
    main()
