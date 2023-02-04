# musica = ['Choram as rosas','Deixa alagar','Conselho','Quando eu ti pela primeira vez']

# print (musica)

# musica.append('Ai se eu te pego') #Adiciona no final da lista
# print (musica)

# print = (len (musica))

#Exemplo 1

# impar = (1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17, 19 )

# print (impar[::2]) #Apresenta a lista toda pulando de 2 em 2
# print (impar[1:3]) #Apresenta a lista somente do 1-2

#Exemplo 2
#Como CLONAR uma lista

lista1 = ['vermelho', 'verde', 'azul']

lista2 = lista1[:]

lista2[0] = 'rosa'

print (f'Lista 1 {lista1}')
print (f'Lista 2 {lista2}')

#Checar se azul esta na lista 1
# if 'azul' in lista1:
#     print ('Esta')
# else:
#     print ('Nao esta')
    
# # Juntar duas listas (concatenação)

#a = lista1 + lista2

# print (a)

# Repetir a letra "n" vezes

#a = a * 3
#print (a)


#Remover da lista na posição "n"
a = [1,2,3,4,5]
print (a)
del a[0]
print (a)