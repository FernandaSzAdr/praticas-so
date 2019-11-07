# -*- coding: utf-8 -*-


class Elevator():
    """docstring for Elevator."""

    def __init__(self, posicoes=None, direcao=0, start_pos=11):
        self.posicoes = posicoes
        self.direcao = direcao
        self.start_pos = start_pos

    def reverse_direcao(self):
        if self.direcao == 0:
            self.direcao = 1
        else:
            self.direcao = 0

    def get_pos(self):
        if self.start_pos and self.direcao == 0:
            pos = list(filter(lambda x: x < self.start_pos, self.posicoes))
            pos = sorted(pos, reverse=True)
        elif self.start_pos and self.direcao == 1:
            pos = list(filter(lambda x: x > self.start_pos, self.posicoes))
            pos = sorted(pos)
        else:
            pos = sorted(self.posicoes)

        return pos

    def acess_pos(self, pos):
        for i in pos:
            print(f'Acessando a posição {i}')
            self.posicoes.remove(i)

    def run(self):
        print('\n***Iniciando leitura de disco***')
        primeira_rodada = True

        while len(self.posicoes) != 0:
            pos = self.get_pos()
            self.acess_pos(pos)

            if primeira_rodada:
                primeira_rodada = False
                self.reverse_direcao()
                print('-------- Direção do elevador foi alterada --------')
            else:
                self.reverse_direcao()
