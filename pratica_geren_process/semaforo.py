# -*- coding: utf-8 -*-

from time import sleep
from threading import Thread, Semaphore


regiao_critica = list(range(5))

semaphore = Semaphore()


class ProcessBase:
    def take_control(self):
        semaphore.acquire()
        print('Process 0{} take the control of the Semaphore'.format(self.id))
        print('Process 0{} see the Semaphore size is {}'.format(self.id,
              semaphore._value))
        print('Process 0{} see len of the "regiao_critica" is {}'.format(
              self.id, len(regiao_critica)))
        """
            Se esse sleep estiver ativado poderá ver que o `semaphore.acquire`
            para a execução do algoritmo, para esperar ate que o semaphore
            esteja disponível.
        """
        sleep(5)

    def is_empty(self):
        global regiao_critica

        if len(regiao_critica) == 0:
            print('Process 0{} is stop, because "regiao_critica" is '
                  'empty.'.format(self.id))
            return True

        return False

    def is_full(self):
        global regiao_critica

        if len(regiao_critica) > 10:
            print('Process 0{} is stop, because "regiao_critica" have more '
                  'then 10 elements.'.format(self.id))
            return True

        return False

    def initialize_proc(self):
        print('Process 0{} is initialize...'.format(self.id))

        """
            Foi inserido essa verificação mas com o intuito de logar, porque
            a classe Semaphore já faz essa verificação e já deixa o processo em
            block.
        """
        if semaphore._value == 0:
            print("Process 0{} can't to take the control! "
                  "The size of the semaphore is {}.".format(self.id,
                                                            semaphore._value))

    def new_len(self):
        print('Process 0{} see new len of the "regiao_critica" is '
              '{}'.format(self.id, len(regiao_critica)))

        """
            Não coloquei esse print após o `semaphore.release()`
            porque em alguns casos ele não aparecia exatamente logo
            após a execução do comando.
        """
        print('Process 0{} finished and change the semaphore size to '
              '{}'.format(self.id, semaphore._value+1))

    def stop(self):
        self.running = False


class ProcessInput(Thread, ProcessBase):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        self.running = True

    def input_element(self):
        global regiao_critica

        self.initialize_proc()

        if self.is_full():
            self.stop()
        else:
            self.take_control()

            if self.is_full():
                semaphore.release()
                self.stop()
            else:
                print('Process 0{} is going to input a element in '
                      '"regiao_critica"'.format(self.id))
                regiao_critica.append(self.id)

                self.new_len()

                semaphore.release()

    def run(self):
        while self.running:
            self.input_element()


class ProcessOutput(Thread, ProcessBase):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        self.running = True

    def output_element(self):
        global regiao_critica

        self.initialize_proc()

        if self.is_empty():
            self.stop()
        else:
            self.take_control()

            if self.is_empty():
                semaphore.release()
                self.stop()
            else:
                print('Process 0{} is going to output a element in '
                      '"regiao_critica"'.format(self.id))
                regiao_critica.pop()

                self.new_len()

                semaphore.release()
                sleep(5)

    def run(self):
        while self.running:
            self.output_element()


if __name__ == '__main__':
    t0 = ProcessOutput(0)
    t1 = ProcessInput(1)
    t2 = ProcessInput(2)
    t3 = ProcessOutput(3)
    t4 = ProcessInput(4)

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t0.join()
    print("Process 00 stoped!")
    t1.join()
    print("Process 01 stoped!")
    t2.join()
    print("Process 02 stoped!")
    t3.join()
    print("Process 03 stoped!")
    t4.join()
    print("Process 04 stoped!")
