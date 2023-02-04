#Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros 
# e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

lista = [2, 2, 3, 4]

def soma_elementos(lista):
    soma = 0
    for c in lista:
        soma += c
    return soma

lista = soma_elementos(lista)
print (lista)