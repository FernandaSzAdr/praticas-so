# -*- coding: utf-8 -*-

import random

from memoria import Memoria
from processo import Processo


def inst_processos():
    memoria = Memoria(512)

    p1 = Processo(1, 'AHH Zeus do céu!', 10, memoria)
    p2 = Processo(2, 'AHH Odin do céu!', 40, memoria)
    p3 = Processo(3, 'AHH Deus do céu!', 250, memoria)
    p4 = Processo(4, 'AHH Hercules do céu!', 90, memoria)
    p5 = Processo(5, 'AHH Atena do céu!', 100, memoria)
    p6 = Processo(6, 'AHH Afrodite do céu!', 3, memoria)
    p7 = Processo(7, 'AHH Cristo do céu!', 30, memoria)
    p8 = Processo(8, 'AHH Thor do céu!', 60, memoria)
    p9 = Processo(9, 'AHH Apolo do céu!', 130, memoria)
    p10 = Processo(10, 'AHH Adonis do céu!', 230, memoria)

    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


if __name__ == '__main__':
    processos = inst_processos()
    choices = ['run', 'stop']
    running = []

    while processos:
        if random.choice(choices) == 'run':
            processo = random.choice(processos)
            if processo not in running:
                processo.run()
                running.append(processo)
        elif random.choice(choices) == 'stop':
            processo = random.choice(processos)
            if processo in running:
                processo.stop()
                running.remove(processo)
                processos.remove(processo)
