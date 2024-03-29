#!/usr/bin/env python3
# The ExamGenerator class.

import random
import os
import glob
import subprocess
import datetime
import sys

class ExamGenerator:
    def __init__(self, q, n, c, quiet, stats, pprint):
        self.q = q
        self.n = n
        self.c = c
        self.quiet = quiet
        self.stats = stats
        self.pprint = pprint

    def gen_exam(self):
        header = r'''
        \documentclass{article}
        \usepackage[a4paper, margin=2cm]{geometry}
        \usepackage[magyar]{babel}
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{enumerate}
        \usepackage{amsmath}
        \usepackage{amssymb}

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
        prefooter = r'''\end{enumerate}
        '''
        footer = r'''
        \end{document}'''

        r = random.sample(self.q, self.n)
        for l in r:
            question = str(l[1])
            category = str(l[0])

            main += str(r'\item ' + question + '\n')

            self.c[category] = self.c[category] + 1

        # Only sort if it's actually needed
        if not self.quiet or self.stats:
            sorted_c = sorted(self.c.items(), key=lambda x: x[1], reverse=True)

        if not self.quiet:
            print("A generált dokumentum feladatai a következő témakörökből "
                    "valók:")
            for i, j in sorted_c:
                if j > 0:
                    print("-", i + ":", j, "példa")

        stats_str = ""
        if self.stats:
            stats_str += r'''\footnotesize\textit{('''

            for i, j in sorted_c:
                if j > 0:
                    stats_str += str(i) + ": " + str(j) + ", "

            stats_str = stats_str[:-2]
            stats_str += r''')}
            '''

        content = header + main + prefooter + stats_str + footer

        randname = str(random.randint(1000, 9999))
        texname = randname + ".tex"

        with open(texname, 'w') as f:
            f.write(content)

        commandLine = subprocess.Popen(['pdflatex', texname],
                stdout=open(os.devnull, 'wb'))
        commandLine.communicate()

        if self.pprint:
            commandLine = subprocess.Popen(['lpr', randname + '.pdf'])
            commandLine.communicate()

        if not self.quiet:
            print(randname + ".pdf létrehozva!")

        os.unlink(randname + ".aux")
        os.unlink(randname + ".log")
        os.unlink(texname)
