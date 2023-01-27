#Receba um número inteiro
#Imprima a soma desses digitos

numero = int(input('Digite um número inteiro: '))
soma = 0

while(numero > 0):
    soma += numero % 10
    numero = int(numero / 10)
print(soma)