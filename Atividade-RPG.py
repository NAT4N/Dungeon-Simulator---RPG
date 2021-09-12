import random

caminho = 0
interação = 0
salaAtual = 1

SALAS = [
    [0],
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 8],
    [7, 8, 9],
    [8, 9, 0]
    ]

while interação < 7:
    try:
        if(salaAtual == 9):
            print("Você está na sala ",salaAtual,": Venceu ! Parabéns !! ")   
            break
        
        elif(salaAtual == 6):
            print("Você está na sala ",salaAtual,": \n Escolha seu caminho ! \n [1] - Caminho Preto")
            caminho = int(input(" "))
            salaAtual = SALAS[salaAtual][caminho]

        print("Você está na sala ",salaAtual,": \n Escolha seu caminho ! \n [1] - Caminho Vermelho \n [2] - Caminho Preto")
        caminho = int(input(" "))
        salaAtual = SALAS[salaAtual][caminho]
        SALAS[8][2] = random.randint(1, 5)
        interação += 1

    except:
        caminho = 0
        print("Caminho Invalido !")

else:
    print("Você perdeu ! Atingiu o nivel maximo de jogadas") 
    