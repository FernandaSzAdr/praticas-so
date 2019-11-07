# -*- coding: utf-8 -*-
from elevator import Elevator


def receive_inputs():
    value = ''
    posicoes = []

    while value != 'exit':
        print('\nPosiçoes válidas de 0 até 39.')
        value = input('-> Informe uma posição (para sair digite "exit"): ')

        if value != 'exit' and value.isdigit():
            value = int(value)
            if value < 40 and value not in posicoes:
                posicoes.append(int(value))
                print(f'Valor {value} salvo nas lista de posições.\n')
            else:
                print('Informe um valor entre 0 e 39.')
        elif value != 'exit' and not value.isdigit():
            print('Informe um valor válido!')
        if value == 'exit' and len(posicoes) == 0:
            print('Você não forneceu nenhuma posição.\n'
                  'O programa encerrou sem ser executado!')

    return posicoes


def up_down():
    correct = ['up', 'down']
    up = ''

    while up not in correct:
        up = input('-> O elevador vai subir ou vai descer? (up ou down)\n')

        print('\n\n')
        if up == 'up':
            return 1
        elif up == 'down':
            return 0
        else:
            print('Não entendi sua resposta. Tente novamente!')


def pos_init():
    correct = ['sim', 'não']
    yes = ''

    while yes not in correct:
        yes = input('-> Você deseja fornecer uma posição inicial?'
                    ' (sim ou não)\n')

        if yes == 'sim':
            start_pos = int(input('->Informe uma posição inicial (0 a 39): '))
        elif yes == 'não':
            start_pos = 11
            print(f'Será utilizada a posição inicial defaul: {start_pos}')
        else:
            print('Não entendi, tente novamente!')

        print('\n\n')

    return start_pos


def main():
    direcao = up_down()
    start_pos = pos_init()
    print('*'*55)
    posicoes = receive_inputs()

    if start_pos is not None:
        if len(posicoes) != 0:
            elevator = Elevator(posicoes=posicoes, direcao=direcao,
                                start_pos=start_pos)
            elevator.run()


if __name__ == '__main__':
    main()
