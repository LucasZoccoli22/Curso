#Programa que leia numeros do teclado
#Quando o Zero for digitado acaba a execução do programa
#Apresente a lista na ordem inversa
lista = []
while True:
    n = int (input ('Digite um número: '))
    if n == 0:
        break
    else :
        lista.append(n)
        
c = len(lista)

#print(list(reversed(lista))) #coloca a lista de traz pra frente

for i in range (c, 0, -1):
    print (i, end= ' ')