# -*- coding: utf-8 -*-

import numpy as np
from time import sleep


class Memoria:

    def __init__(self, size):
        self.bitmap = np.zeros((size))

    def espaco_livre(self):
        return len(np.where(self.bitmap == 0)[0])

    def get_pos(self):
        """
            Captura todas as posições que tenham valor zero.

            ex: bitmap = array([1., 1., 1., 1., 0., 0., 0., 1., 1., 0.])
                pos = [[4, 5, 6], [9]]
        """

        is_zero = np.where(self.bitmap == 0)[0]

        pos = []
        pos_i = []

        for i in is_zero:
            if len(pos_i) == 0:
                pos_i.append(i)
            else:
                if pos_i[-1] == i - 1:
                    pos_i.append(i)
                else:
                    pos.append(pos_i)
                    pos_i = [i]
                    if is_zero[-1] == i:
                        pos.append(pos_i)

        if len(pos) == 0:
            pos.append(pos_i)

        return pos

    def pos_livre(self, size_need):
        """
            A partir de uma lista ([[4, 5, 6], [9]]), extrai uma região
            possível para alocar o processo que será executado. No caso, uma
            posição que tenha o mesmo tamanho do processo ou que seja maior.

            O retorno será a posição inicial e final dessa região que será
            utilizada. Caso não encontre uma região possível, o retorno será
            vazio.
        """

        pos = self.get_pos()

        for p in pos:
            """
                Procura-se a primeira região dispónivel, ela deverá ser de
                tamanho igual ou maior do que a região necessária.
            """
            if len(p) == size_need or len(p) > size_need:
                return p

        return None

    def aloca_espaco(self, size):
        pos = self.pos_livre(size)

        if not pos:
            return None
        else:
            self.bitmap[pos[0]:pos[0]+size] = 1
            return[pos[0], pos[0]+size]

    def desaloca_espaco(self, espaco):
        if not espaco:
            return False
        else:
            self.bitmap[espaco[0]:espaco[1]] = 0
            return True


class Processo:

    def __init__(self, id, mensagem, size, memoria):
        self.id = id
        self.mensagem = mensagem
        self.size = size
        self.espaco = None
        self.memoria = memoria

    def process_run(self):
        print('O processo 0{} foi alocado com sucesso na posição {}:{}'.
              format(self.id, self.espaco[0], self.espaco[1]))

        sleep(2)
        print('******'
              ' {} espaços foram alocados na memoria! '
              '******'.format(self.size))
        print('******'
              ' {} espaços disponiveis na memória! '
              '******'.format(self.memoria.espaco_livre()))

        sleep(2)
        print(self.mensagem)
        print('\n')
        sleep(3)

    def run(self):
        self.espaco = self.memoria.aloca_espaco(self.size)

        if self.espaco:
            print('Processo {} será executado!'.format(self.id))
            self.process_run()
        else:
            print('Não foi possível alocar o processo {}. '
                  'Não tem espaço disponível'.format(self.id))
            print('\n')

    def stop(self):
        if self.memoria.desaloca_espaco(self.espaco):
            print('Processo 0{} foi encerrado!'.format(self.id))
            print('Memoria liberada na posição {}:{}'.format(self.espaco[0],
                  self.espaco[1]))
            print('\n')
            sleep(3)
        else:
            print('Processo 0{} não está em execução!'.format(self.id))
            print('\n')
            sleep(3)


if __name__ == '__main__':
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

    p1.run(); p2.run(); p3.run(); p1.stop(); p3.stop(); p4.run(); p5.run()
    p2.stop(); p4.stop(); p6.run(); p7.run(); p8.run(); p9.run(); p10.run()
