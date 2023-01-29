#Função que recebe dois valores
#Imprime o maior

def maximo(x,y):
    if x > y:
        maior = x
    elif y > x:
        maior = y
    else :
        maior = x
    return maior



print (maximo (3,4))
print (maximo (0,-1))
print (maximo (7,7))
