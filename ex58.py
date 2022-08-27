from random import randint
computador = randint(0,10)
print('Olá, sou seu computador! Será que consegue advinhar qual é o número de 0 a 10?: ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou! Com {} palpites'.format(palpites))


