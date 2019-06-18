#!/usr/bin/env python3

import random
import os
import glob
import subprocess
import datetime
import sys

def gen_exam(q, n): # q is the array that holds the questions and n is the number how many questions we want in an exam
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
    \maketitle
    \begin{center}\Large\textsc{Feladatok}\end{center}
    \begin{enumerate}
        \setlength\itemsep{0em}
    '''
    main = ''
    footer = r'''\end{enumerate}
    \end{document}'''

    r = random.sample(q, n)
    for l in r:
        main += str('\\item ' + l + '\n')

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

    n = 16

    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except:
            usage()


    with open("q.txt", "r") as f:
        for line in f:
            q.append(line)

    print(len(q), "kérdés betöltve!")
    print(str(n) + " db kérdést tartalmazó dolgozat folyamatban...")
    gen_exam(q, n)

main()
