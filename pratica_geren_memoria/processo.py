# -*- coding: utf-8 -*-

from time import sleep


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
