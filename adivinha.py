import random
from random import randint

print('**********************')
print("Joguin de Adivinhação!")
print('**********************')

numero = random.randint(1,100)

print(numero
      )

chute = int(input("Qual o seu chute? "))
if chute == 57:
    print("ACERTOU!!")
if chute < 57:
    print("Mais pra cima")
if chute > 57:
    print("Mais pra baixo")



while chute != numero:
    chute = int(input("Qual o seu chute? "))
    if chute == numero:
        print("ACERTOU!!")
    if chute < numero:
        print("Mais pra cima")
    if chute > numero:
        print("Mais pra baixo")
    fraco = input("Você desiste? ")
    if(fraco[0:] == 's'):
        print("O número era: {}".format(numero))
        break
    else:
        continue

