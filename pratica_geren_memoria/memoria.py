# -*- coding: utf-8 -*-

import numpy as np


class Memoria:

    def __init__(self, size):
        self.bitmap = np.zeros((size))

    @property
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
