#Receba um número inteiro positivo 
#Imprima "primo" ou "não primo"

n = int(input('Digite um número inteiro: '))

total = 0

for c in range(1, n + 1):
    if n % c == 0:
        total += 1
    
if total > 2:
    print ('não primo')
else:
    print ('primo')