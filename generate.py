#!/usr/bin/env python3

import random
import os
import glob
import subprocess
import datetime

def gen_exam(q):
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
    \begin{document}
    \maketitle
    \begin{enumerate}
    '''
    main = ''
    footer = r'''\end{enumerate}
    \end{document}'''

    r = random.sample(q, 16)
    for l in r:
        main += str('\item ' + l + '\n')

    content = header + main + footer

    randname = str(random.randint(1000, 9999))
    texname = randname + ".tex"

    with open(texname, 'w') as f:
        f.write(content)

    commandLine = subprocess.Popen(['pdflatex', texname])
    commandLine.communicate()

    os.unlink(randname + ".aux")
    os.unlink(randname + ".log")
    os.unlink(texname)

def main():
    q = []

    with open("q.txt", "r") as f:
        for line in f:
            q.append(line)

    print(len(q), "kérdés betöltve! Sorsolás folyamatban...")
    gen_exam(q)

main()
