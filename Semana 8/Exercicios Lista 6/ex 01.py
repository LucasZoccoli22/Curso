#Escreve uma função remove_repetidos

lista = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(lista):
    lista2 = [] #Clonou a lista original
    for i in lista:
        if i not in lista2: #comparou a original com o clone
            lista2.append(i)
    lista2.sort()
    return lista2



lista = remove_repetidos(lista)
print (lista)