# -*- coding: utf-8 -*-

"""
    Autor: Maria Fernanda Souza Andrade
"""

from time import sleep
from threading import Thread


flag = [False, False]
turn = 0
regiao_critica = list(range(5))


class Process(Thread):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        self.running = True

    def critical_section(self):
        global regiao_critica

        print('Process 0{} is get in the critical section!'.format(self.id))
        print('Process 0{} see len of the "regiao_critica" is {}'.format(
              self.id, len(regiao_critica)))
        sleep(5)
        if len(regiao_critica) == 0:
            print('Process 0{} is get of the critical section and stop, '
                  'because "regiao_critica" is empty now!'.format(self.id))
            self.stop()
        else:
            print('Process 0{} is going to pop the "regiao_critica"'.format(
                  self.id))
            regiao_critica.pop()
            print('Process 0{} removed one element from the "regiao_critica"'
                  '- len actual is {}'.format(self.id, len(regiao_critica)))
            sleep(5)
            print('Process 0{} is get of the critical section!'.format(self.id))

    def process_run(self):
        global flag
        global turn
        global regiao_critica

        print('Process 0{} initialize...'.format(self.id))

        if len(regiao_critica) == 0:
            print('Process 0{} is stop, because "regiao_critica" is '
                  'empty.'.format(self.id))
            self.stop()

        else:
            flag[self.id] = True
            turn = 1 - self.id

            while flag[turn] and turn != self.id:
                print('Process 0{} waiting for the process 0{}'.format(
                      self.id, turn))
                sleep(2)

            self.critical_section()

            flag[self.id] = False

            print('Process 0{} finish...'.format(self.id))

    def run(self):
        while self.running:
            self.process_run()

    def stop(self):
        self.running = False


if __name__ == '__main__':
    t0 = Process(0)
    t1 = Process(1)

    t0.start()
    t1.start()

    t0.join()
    print("Process 00 stoped!")
    t1.join()
    print("Process 01 stoped!")
