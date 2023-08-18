# Python program to display the Fibonacci sequence
#Sistema de troco
moedas = [100, 50, 25, 10, 5, 1]
total = 0
troco = int(input("Valor do troco: "))

for i in range(len(moedas)):
    nMoedas = troco // moedas[i]
    troco -= nMoedas * moedas[i]
    total += nMoedas

print(f'Total de moedas recebidas: {total}')