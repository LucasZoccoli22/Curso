#Dado um numero primo
#Imprima sua multiplicação/fatoração

n = int(input('Digite um numero >1: '))

fator = 2
mult = 0

while n > 1:
    while n % fator == 0:
        mult += 1
        n = n / fator
    if mult > 0:
        print (f'Fator {fator} multiplicidade = {mult}')
    fator += 1
    mult = 0