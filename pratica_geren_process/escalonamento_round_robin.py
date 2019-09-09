# -*- coding: utf-8 -*-

from time import sleep


"""
    A classe Thread de python não permite implementar prioridade, grupo de
    therad e elas não podem ser dsstruidas, interrompidas, suspensas.

    Irei implementar 'processos' que possuem `priority`, que será utilizada
    para ordenar a lista em quanto estiver processos para executar. Os
    processos não serão heardados da classe Thread, são processos abstratos.

    OBS: Como não consigo limitar a duração de threds em Python, irei reduzir
    a prioridade das threads até que chegem em 1. Caso a prioridade sejá 1,
    será removido após a execução.
"""


class Process:

    def __init__(self, name, priority, message):
        self.name = name
        self.priority = priority
        self.message = message
        self.finish = False

    def run(self):
        """
            Todos os 'processos' iram executar na mesma faixa de tempo
        """
        print('Process {} is running, priority is {}!!!'.format(self.name,
              self.priority))
        print('See the message: {}'.format(self.message * self.priority))
        sleep(1)


def create_list():
    list_process = []

    list_process.append(Process(name=1, priority=4, message='Process 1 '))
    list_process.append(Process(name=2, priority=1, message='Process 2 '))
    list_process.append(Process(name=3, priority=2, message='Process 3 '))
    list_process.append(Process(name=4, priority=1, message='Process 4 '))
    list_process.append(Process(name=5, priority=3, message='Process 5 '))
    list_process.append(Process(name=6, priority=1, message='Process 6 '))
    list_process.append(Process(name=7, priority=2, message='Process 7 '))
    list_process.append(Process(name=8, priority=4, message='Process 8 '))
    list_process.append(Process(name=9, priority=3, message='Process 9 '))
    list_process.append(Process(name=10, priority=2, message='Process 10 '))

    return list_process


if __name__ == '__main__':
    list_process = create_list()

    while len(list_process) != 0:
        print('='*60)

        list_process = [p for p in list_process if not p.finish]
        list_process.sort(key=lambda proc: proc.priority, reverse=True)
        for process in list_process:
            process.run()

            if process.priority == 1:
                process.finish = True
            else:
                process.priority = process.priority - 1

    print('Finish!!')
