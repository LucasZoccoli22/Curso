#Leia uma sequencia de numero
#Acaba no 0
#Imprima na ordem inversa, onde o 0 nao aparece

lista = []
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    else:
        lista.append(n)
        
a = (list(reversed(lista)))

for i in a:
    print(i)
    