#!/usr/bin/env python3

import random
import os
import glob
import subprocess
import datetime
import sys
import collections

def gen_exam(q, n, c): # q is the array that holds the questions and n is the number how many questions we want in an exam
    header = r'''
    \documentclass{article}
    \usepackage[a4paper, margin=2cm]{geometry}
    \usepackage[magyar]{babel}
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage{enumerate}
    \usepackage{amsmath}

    \setlength{\parindent}{0em}
    \title{Kalkulus mintavizsga}
    \date{\today}

    \pagenumbering{gobble}

    \begin{document}

    \begin{center}
        \LARGE Kalkulus mintavizsga\\[1em]
        \large\today\\[1em]
        \Large\textsc{Feladatok}
    \end{center}

    \begin{enumerate}
        \setlength\itemsep{0em}
    '''
    main = ''
    footer = r'''\end{enumerate}
    \end{document}'''

    r = random.sample(q, n)
    for l in r:
        question = str(l[1])
        category = str(l[0])

        main += str(r'\item ' + question + '\n')

        c[category] = c[category] + 1

    print("A generált dokumentum feladatai a következő témakörökből valók:")
    for i in collections.OrderedDict(c):
        if c[i] > 0:
            print("-", i + ":", c[i], "példa")

    content = header + main + footer

    randname = str(random.randint(1000, 9999))
    texname = randname + ".tex"

    with open(texname, 'w') as f:
        f.write(content)

    commandLine = subprocess.Popen(['pdflatex', texname], stdout=open(os.devnull, 'wb'))
    commandLine.communicate()

    print(randname + ".pdf létrehozva!")

    os.unlink(randname + ".aux")
    os.unlink(randname + ".log")
    os.unlink(texname)

def usage():
    print("Használat: " + sys.argv[0] + " [kérdések száma]")

def main():
    q = []
    c = {}

    n = 16

    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except:
            usage()

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

    gen_exam(q, n, c)

main()
