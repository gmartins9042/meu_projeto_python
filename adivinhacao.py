import random

def jogar():

    print("**********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101) #0.0 1.0
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print('Qual nivel de dificuldade?', numero_secreto)
    print('(1) Facíl (2) Médio (3) Difícil')

    nivel = int(input("Defina o nível:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')

        chute = int(input('Digite um número de 1 a 100: '))
        print("Você digitou", chute)

        if(chute < 1 or  chute > 100):
            print('Você deve digitar um número de 1 a 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou, O seu chute foi maior do que o numero secreto')
            elif(menor):
                print('Você errou, O seu chute foi menor do que o numero secreto')
            pontos_perdidos = abs(numero_secreto - chute)# 40 - 20
            pontos = pontos - pontos_perdidos


        print("Fim do Jogo!")
if(__name__== '__main__'):
    jogar()