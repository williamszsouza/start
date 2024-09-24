import time as tm
import random 
import os




decisoes = ['pedra','papel','tesoura']

def menu():
    print("BEM VINDO AO JOKEMPO")
    print("DIGITE (0) PARA ESCOLHER PEDRA")
    print("DIGITE (1) PARA ESCOLHER PAPEL")
    print("DIGITE (2) PARA ESCOLHER TESOURA")
    

def resultados():
    empate = False
    maquina_vencedor = False
    jogador_vencedor = False
    while True:
        try:
            jogador = int(input("Digite a sua escolha: "))
            if jogador >= 0 and jogador < 3:
                break
                
            else:
             print("Insira um numero entre 0 e 2")
        except ValueError:
            print("Insira um numero inteiro!!")
    maquina = random.randrange(0,3)
    
    if maquina == 0:
        maquina = decisoes[0]
    elif maquina == 1:
        maquina = decisoes[1]
    elif jogador == 2:
        maquina = decisoes[2]
    

    if jogador == 0:
        jogador = decisoes[0]
    elif jogador == 1:
        jogador = decisoes[1]
    elif jogador == 2:
        jogador = decisoes[2]
    
    if jogador == decisoes[0] and maquina == decisoes[1] or jogador == decisoes[1] and maquina == decisoes[2] or jogador == decisoes[2] and maquina == decisoes[0]:
        maquina_vencedor = True
    elif jogador == maquina:
        empate = True
    else:
        jogador_vencedor = True    

    if empate == True:
        os.system('cls')
        print(f"Você escolheu: {jogador}")
        print(f"A maquina escolheu: {maquina}")
        print("O jogo empatou!!")
    elif jogador_vencedor == True:
        os.system('cls')
        print(f"Você escolheu: {jogador}")
        print(f"A maquina escolheu: {maquina}")
        print("Você venceu!!")
    else: 
        os.system('cls')
        print(f"Você escolheu: {jogador}")
        print(f"A maquina escolheu: {maquina}")
        print("A maquina venceu!!")
        tm.sleep(2)
    return empate or maquina_vencedor or jogador_vencedor

while True:
    os.system("cls")
    menu()
    print('JO')
    tm.sleep(1)
    print("KEN")
    tm.sleep(1)
    print("PO!")
    resultados()



