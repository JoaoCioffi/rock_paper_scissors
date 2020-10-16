"""

                    .::. Python mini-game .::.
                    
                     ('Rock-Paper-Scissors')

"""
print('\n')
print(' ~ ' * 30)
print('\n')

import __hello__
from random import random
import time

name = input('\nInsira seu nome: ')
name = name.title()

def rock_paper_scissors():
        
    print(f'\nBem-Vindo(a), {name}!')
    
    print('\nEssa função faz uma escolha entre \'PEDRA\', \'PAPEL\' ou \'TESOURA\' de forma randômica')    
    decision = int(float(input('\nVocê deseja jogar? Insira \'1\' para jogar ou \'0\' para sair do jogo: ')))
    
    if decision == 1:
        
        time.sleep(1)
        print('\nInicializando jogo ...')
        time.sleep(1)
        
        choice_player = input('\nPor favor, digite \'PEDRA\', \'PAPEL\' ou \'TESOURA\' -> ')
        choice_player = choice_player.upper()
        
        choice_machine = ['PEDRA', 'PAPEL', 'TESOURA']
        
        winner_status = 'você ganhou =)'
        draw_status ='deu empate!'
        loser_status = 'você perdeu =('
        
        value = random()  #-> Faz uma escolha randômica entre 0 e 1
        
        if 0 <= value < (1/3):
            read_choice_machine = choice_machine[0]  #-> Máq: PEDRA
            print(f'\nEscolha de {name}: {choice_player} | Escolha da máquina: {read_choice_machine}')
            
            if choice_player == choice_machine[0]:     #-> Plyr: PEDRA
                print(f'\n{name}, {draw_status}')
            
            elif choice_player == choice_machine[1]:   #-> Plyr: PAPEL
                print(f'\n{name}, {winner_status}')
            
            else:                                      #-> Plyr: TESOURA
                print(f'\n{name}, {loser_status}')

        if (1/3) <= value < (2*(1/3)):
            read_choice_machine = choice_machine[1]  #-> Máq: PAPEL
            print(f'\nEscolha de {name}: {choice_player} | Escolha da máquina: {read_choice_machine}')
            
            if choice_player == choice_machine[0]:     #-> Plyr: PEDRA
                print(f'\n{name}, {loser_status}')
            
            elif choice_player == choice_machine[1]:   #-> Plyr: PAPEL
                print(f'\n{name}, {draw_status}')
            
            else:                                      #-> Plyr: TESOURA
                print(f'\n{name}, {winner_status}')
        
        if (2*(1/3)) <= value <= 1:
            read_choice_machine = choice_machine[2]  #-> Máq: TESOURA
            print(f'\nEscolha de {name}: {choice_player} | Escolha da máquina: {read_choice_machine}')
            
            if choice_player == choice_machine[0]:     #-> Plyr: PEDRA
                print(f'\n{name}, {winner_status}')
            
            elif choice_player == choice_machine[1]:   #-> Plyr: PAPEL
                print(f'\n{name}, {loser_status}')
            
            else:                                      #-> Plyr: TESOURA
                print(f'\n{name}, {draw_status}')
            
        
    elif decision == 0:
        print('\nVocê decidiu sair do jogo!')
    
    else:
        print('\nNúmero inválido! Processo finalizado ...')

rock_paper_scissors()

print('\n')
print(' ~ ' * 30)
print('\n')
