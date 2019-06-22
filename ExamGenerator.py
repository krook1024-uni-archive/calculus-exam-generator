#!/usr/bin/env python3
# The ExamGenerator class.

import random
import os
import glob
import subprocess
import datetime
import sys

class ExamGenerator:
    def __init__(self, q, n, c, quiet, stats):
        self.q = q
        self.n = n
        self.c = c
        self.quiet = quiet
        self.stats = stats

    def gen_exam(self):
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

        r = random.sample(self.q, self.n)
        for l in r:
            question = str(l[1])
            category = str(l[0])

            main += str(r'\item ' + question + '\n')

            self.c[category] = self.c[category] + 1

        if not self.quiet:
            print("A generált dokumentum feladatai a következő témakörökből valók:")
            for i in self.c.keys():
                if self.c[i] > 0:
                    print("-", i + ":", self.c[i], "példa")

        content = header + main + footer

        randname = str(random.randint(1000, 9999))
        texname = randname + ".tex"

        with open(texname, 'w') as f:
            f.write(content)

        commandLine = subprocess.Popen(['pdflatex', texname], stdout=open(os.devnull, 'wb'))
        commandLine.communicate()

        if not self.quiet:
            print(randname + ".pdf létrehozva!")

        os.unlink(randname + ".aux")
        os.unlink(randname + ".log")
        os.unlink(texname)

    def usage(self):
        print("Használat: " + sys.argv[0] + " [kérdések száma]")
        print("Kapcsolók:")
        print("--quiet - parancssori kimenet nélküli üzemmőd")
        print("--stats - statisztikák beágyazása a generált dolgozatba")
