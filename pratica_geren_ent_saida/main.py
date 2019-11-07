# -*- coding: utf-8 -*-
from elevator import Elevator


def receive_inputs():
    value = ''
    posicoes = []

    while value != 'exit':
        print('\nPosiçoes válidas de 0 até 39.')
        value = input('Informe uma posição (para sair digite "exit"): ')

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


def main():
    posicoes = receive_inputs()

    elevator = Elevator(posicoes=posicoes, direcao=1, start_pos=11)
    elevator.run()


if __name__ == '__main__':
    main()
