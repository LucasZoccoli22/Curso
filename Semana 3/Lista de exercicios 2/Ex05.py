#Receba 3 números inteiros
#Se for ordem crescete, printa crescente
#Se não "não está em ordem crescente"

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o tericeiro número: '))

if n3>n2>n1:
    print('crescente')
else:
    print("não está em ordem crescente")